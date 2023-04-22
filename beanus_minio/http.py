#  Copyright (c) by The Bean Family, 2023.
#
#  License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
#  These code are maintained by The Bean Family.
import logging
import os

import werkzeug
from minio import Minio

from odoo import http
from odoo.http import request, root
from odoo.tools import config

_logger = logging.Logger(__name__)

#Override the from_attachment function to show the s3 files
# class Stream(http.Stream):
minio_client = Minio(endpoint=config.get('attachment_minio_host'),
                   access_key=config.get('attachment_minio_access_key'),
                   secret_key=config.get('attachment_minio_secret_key'),
                   secure=config.get('attachment_minio_secure'),
                   region=config.get('attachment_minio_region'))
@classmethod
def from_attachment(cls, attachment):
        """ Create a :class:`~Stream`: from an ir.attachment record. """
        attachment.ensure_one()

        self = cls(
            mimetype=attachment.mimetype,
            download_name=attachment.name,
            conditional=True,
            etag=attachment.checksum,
        )

        if attachment.store_fname:
            if "s3" in attachment.store_fname:

                self.type = 'url'
                print(f"s3 path running...{self.type}")
                # TODO: study how to use config.py
                # host = config.get('attachment_minio_host')
                # secure = config.get('attachment_minio_secure')
                # is_https = "https://" if config.get('attachment_minio_secure') == None \
                #                          or config.get('attachment_minio_secure') == True else "http://"
                # _logger.debug(f" host is {host} - scheme is {is_https}")


                file_path = str(attachment.store_fname).replace("s3://", "").split("/")
                print(f"file_path = {file_path}")
                self.url = cls.minio_client.presigned_get_object(f'{file_path[0]}', f'{file_path[1]}/{file_path[2]}')
                print(f"self.url : {self.url}")
                # self.url = f"{is_https}{config.get('attachment_minio_host')}" \
                #            f"{str(attachment.store_fname).replace('s3:/', '')}"
                # _logger.debug(f"self.url : {self.url}")
            else:
                self.type = 'path'
                self.path = werkzeug.security.safe_join(
                    os.path.abspath(config.filestore(request.db)),
                    attachment.store_fname
                )
                stat = os.stat(self.path)
                self.last_modified = stat.st_mtime
                self.size = stat.st_size

        elif attachment.db_datas:
            self.type = 'data'
            self.data = attachment.raw
            self.last_modified = attachment['__last_update']
            self.size = len(self.data)

        elif attachment.url:
            # When the URL targets a file located in an addon, assume it
            # is a path to the resource. It saves an indirection and
            # stream the file right away.
            static_path = root.get_static_file(
                attachment.url,
                host=request.httprequest.environ.get('HTTP_HOST', '')
            )
            if static_path:
                self = cls.from_path(static_path)
            else:
                self.type = 'url'
                self.url = attachment.url

        else:
            self.type = 'data'
            self.data = b''
            self.size = 0

        return self

http.Stream.minio_client = minio_client
http.Stream.from_attachment = from_attachment

