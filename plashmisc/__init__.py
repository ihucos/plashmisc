from plash import utils
from plash.eval import register_macro, eval

UBUNTU_URL_TEMPL = 'https://partner-images.canonical.com/core/{}/current/ubuntu-{}-core-cloudimg-amd64-root.tar.gz'

@register_macro()
def from_ubuntu(version):
    import subprocess
    url = UBUNTU_URL_TEMPL.format(version, version)
    base =  subprocess.check_output(['plash', 'build', '--from-url', url]).decode().rstrip('\n')
    return eval([['from', base]])
