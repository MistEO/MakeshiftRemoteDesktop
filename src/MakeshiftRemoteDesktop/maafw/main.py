import numpy
from typing import Optional

from maa.controller import (
    Win32Controller,
    MaaWin32ScreencapMethodEnum,
    MaaWin32InputMethodEnum,
)
from maa.tasker import Tasker, TaskDetail
from maa.resource import Resource


def main():
    controller = Win32Controller(
        None, MaaWin32ScreencapMethodEnum.DXGI_DesktopDup, MaaWin32InputMethodEnum.Seize
    )
    controller.set_screenshot_use_raw_size(True)
    controller.post_connection().wait()
    img: numpy.ndarray = controller.post_screencap().wait().get()
    print(img.shape)

    resource = Resource()
    resource.post_path("install/maafw_resource").wait()
    tasker = Tasker()
    tasker.bind(resource, controller)
    if not tasker.inited:
        print("Failed to init tasker")
        return

    detail: Optional[TaskDetail] = (
        tasker.post_pipeline("OCR", {"OCR": {"recognition": "OCR"}}).wait().get()
    )
    if not detail:
        print("Failed to get OCR result")
        return
    
    print(detail.nodes[0].recognition.all_results)


if __name__ == "__main__":
    main()
