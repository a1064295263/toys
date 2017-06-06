import datetime

def girlfriend():

    last = datetime.datetime.strptime('2017-05-22 00:00:00', '%Y-%m-%d %H:%M:%S')
    now = datetime.datetime.now()
    while now > last:
        last = last + datetime.timedelta(days=28)
    last = last - datetime.timedelta(days=28)
    during = last + datetime.timedelta(days=7)
    print("\n尊敬的陈同学: ")
    if now < during:
        print(">> 你的女朋友小姨妈大驾光临，距今已经: {}".format(now - last))
    else:
        print(">> 你的女朋友安然无恙，请继续你的表演! ")
    print(">> 上次光临时间为: {}".format(last))
    print(">> 下次光临时间为: {}".format(last + datetime.timedelta(days=28)))

if __name__ == "__main__":
    girlfriend()