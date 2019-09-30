import os
import sys
import sgtk

HookBaseClass = sgtk.get_hook_baseclass()

class ExternalScreenshot(HookBaseClass):
    def capture_screenshot(self, path):
        if sys.platform == "darwin":
            # use built-in screenshot command on the mac
            ret_code = os.system("screencapture -m -i -s %s" % path)
            if ret_code != 0:
                raise sgtk.TankError("Screen capture tool returned error code %s" % ret_code)

        elif sys.platform == "linux2":
            # use image magick
            ret_code = os.system("import %s" % path)
            if ret_code != 0:
                raise sgtk.TankError("Screen capture tool returned error code %s. "
                                     "For screen capture to work on Linux, you need to have "
                                     "the imagemagick 'import' executable installed and "
                                     "in your PATH." % ret_code)

        else:
            raise sgtk.TankError("Unsupported platform.")
