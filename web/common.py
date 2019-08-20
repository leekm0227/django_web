from django.views.generic import View as BaseView
from django.conf import settings
from django.shortcuts import render
from Crypto.Cipher import AES
from Crypto import Random
import hashlib
import base64
import requests

bs = 32
key = hashlib.sha256(settings.SECRET_KEY[:32].encode()).digest()


class View(BaseView):
    token = None
    template = 'index'
    header = {'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8'}
    context = {}

    def get(self, request, **kwargs):
        return render(request, self.template, self.context)

    def dispatch(self, request, *args, **kwargs):
        if 'token' in request.COOKIES:
            self.token = self.dec(request.COOKIES['token'])

        return super().dispatch(request, *args, **kwargs)

    def api(self, method='get', uri=None, data=None):
        if self.token is not None:
            self.header['Authorization'] = "Token " + self.token

        res = requests.request(method, settings.API_URL + uri, data=data, headers=self.header)

        try:
            res.raise_for_status()
        except requests.HTTPError as e:
            print(e)
            return None

        return res.json()

    def enc(self, raw):
        raw = self._pad(raw)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(key, AES.MODE_CBC, iv)
        return base64.b64encode(iv + cipher.encrypt(raw)).decode('utf-8')

    def dec(self, enc):
        enc = base64.b64decode(enc)
        iv = enc[:AES.block_size]
        cipher = AES.new(key, AES.MODE_CBC, iv)
        return self._unpad(cipher.decrypt(enc[AES.block_size:]))

    @staticmethod
    def _pad(s):
        return bytes(s + (bs - len(s) % bs) * chr(bs - len(s) % bs), 'utf-8')

    @staticmethod
    def _unpad(s):
        return s[:-ord(s[len(s) - 1:])].decode('utf-8')
