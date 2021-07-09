import os
import shutil
import cv2


def video_to_images(video_path: str, images_save_path: str,
                    frame_per_second: int):

    # if not os.path.exists(images_save_path):
    #     os.mkdir(images_save_path)
    # else:
    #     shutil.rmtree(images_save_path)
    #     os.mkdir(images_save_path)

    video_name = video_path.split('/')[-1].split('.')[0]

    # 读取视频文件
    videoCapture = cv2.VideoCapture(video_path)
    # 计算图片的帧率
    fps = videoCapture.get(cv2.CAP_PROP_FPS)
    # 按帧读取视频，成功为sucess返回True，为img返回三维矩阵
    success, frame = videoCapture.read()
    # 已读帧数
    frame_count = 0
    # 已保存帧数
    save_frame_count = 0

    # 当成功读取到一帧后
    while success:
        # 当累计帧数为你想要的帧率的倍数时，再进行图片处理操作！
        if frame_count % int(fps / frame_per_second) == 0:
            save_frame_count += 1
            # 保存抽出的帧
            # cv2.imwrite(images_save_path + "%d.jpg" % save_frame_count,
            #             frame)
            cv2.imencode('.jpg', frame)[1].tofile(images_save_path +
                                                  "%d.jpg" % save_frame_count)

        # 再读取下一帧
        success, frame = videoCapture.read()
        frame_count += 1


def get_name_by_ext(path, ext_name):
    name_list = list()
    for root, dirs, names in os.walk(path):
        for name in names:
            ext = os.path.splitext(name)[1]  # 获取后缀名
            if ext == ext_name:
                name_list.append(name)
    return name_list


if __name__ == "__main__":
    pass