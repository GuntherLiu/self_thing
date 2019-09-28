import time
import os

class Dir:
    def __init__(self, downloadtype):

        type_dict = {
            "yazhouwuma": 2,
            "yazhouyouma": 15,
            "oumeiyuanchuang": 4,
            "dongmanyuanchuang": 5,
            "guochanyuanchuang": 25,
            "zhongziyuanchuang": 26,
        }
        if downloadtype in type_dict.keys():
            self.fid = type_dict[downloadtype]
        else:
            raise ValueError("type wrong!")

        # if not exist torrent_dir, then create it
        now_time = time.strftime("%Y-%m-%d_%H-%M", time.localtime())
        self.dir_name = "torrent_dir_" + downloadtype + now_time
        os.makedirs(self.dir_name)