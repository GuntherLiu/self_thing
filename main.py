from constant import Dir
from crawl import Crawl
from file_zip import DoZip
import threading
from send_email import Email


def run():
    list = ["yazhouwuma", "yazhouyouma", "oumeiyuanchuang", "dongmanyuanchuang", "guochanyuanchuang", "zhongziyuanchuang"]
    for type in list:
        print type + "start!"
        create_dir(type)


def create_dir(type):
    print "create dir"
    dir = Dir(type)

    crawl_torrent(dir)


def crawl_torrent(dir):
    print "crawl torrent"
    crawl = Crawl(dir.dir_name)
    crawl.start(dir.fid, 1, 5, 5)

    do_zip(dir)


def do_zip(dir):
    print "do zip"
    zip_util = DoZip()
    file_name = dir.dir_name+".zip"
    zip_util.do_zip(file_name, dir.dir_name)

    t = threading.Thread(target=send_email, args=(file_name,))
    t.start()


def send_email(file_name):
    print "zend email"
    fromaddr = 'qiezi12368@163.com'
    password = '2967posy'
    toaddrs = ['qiezi12368@163.com']

    mail = Email()
    mail.send(file_name,fromaddr,password,toaddrs)


if __name__ == '__main__':
    run()

