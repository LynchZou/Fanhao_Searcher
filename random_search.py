import random


"""
randomly select 1 url to search
"""
def selectURL():

    allURl = []

    # Nippon Animation Meisaku
    allURl.append("http://www.nippon-animation.co.jp/work/1893/")
    allURl.append("http://www.nippon-animation.co.jp/work/1875/")
    allURl.append("http://www.nippon-animation.co.jp/work/1859/")
    allURl.append("http://www.nippon-animation.co.jp/work/1791/")
    allURl.append("http://www.nippon-animation.co.jp/work/1765/")
    allURl.append("http://www.nippon-animation.co.jp/work/1751/")
    allURl.append("http://www.nippon-animation.co.jp/work/1730/")
    allURl.append("http://www.nippon-animation.co.jp/work/1713/")
    allURl.append("http://www.nippon-animation.co.jp/work/1678/")
    allURl.append("http://www.nippon-animation.co.jp/work/1658/")
    allURl.append("http://www.nippon-animation.co.jp/work/1627/")
    allURl.append("http://www.nippon-animation.co.jp/work/1601/")
    allURl.append("http://www.nippon-animation.co.jp/work/1582/")
    allURl.append("http://www.nippon-animation.co.jp/work/1558/")
    allURl.append("http://www.snippon-animation.co.jp/work/1532/")
    allURl.append("http://www.nippon-animation.co.jp/work/1511/")
    allURl.append("http://www.nippon-animation.co.jp/work/1486/")
    allURl.append("http://www.nippon-animation.co.jp/work/1473/")
    allURl.append("http://www.nippon-animation.co.jp/work/1446/")
    allURl.append("http://www.nippon-animation.co.jp/work/1423/")
    allURl.append("http://www.nippon-animation.co.jp/work/1408/")
    allURl.append("http://www.nippon-animation.co.jp/work/1387/")
    allURl.append("http://www.nippon-animation.co.jp/work/1370/")
    allURl.append("http://www.nippon-animation.co.jp/work/1307/")
    allURl.append("http://www.nippon-animation.co.jp/work/1285/")
    allURl.append("http://www.nippon-animation.co.jp/work/1061/")
    allURl.append("http://www.nippon-animation.co.jp/work/962/")
    allURl.append("http://www.nippon-animation.co.jp/work/843/")

    # Nippon Animation Family
    allURl.append("http://www.nippon-animation.co.jp/work/5808/")
    allURl.append("http://www.nippon-animation.co.jp/work/5858/")
    allURl.append("http://www.nippon-animation.co.jp/work/5884/")
    allURl.append("http://www.nippon-animation.co.jp/work/6078/")
    allURl.append("http://www.nippon-animation.co.jp/work/5807/")
    allURl.append("http://www.nippon-animation.co.jp/work/4139/")
    allURl.append("http://www.nippon-animation.co.jp/work/6085/")
    allURl.append("http://www.nippon-animation.co.jp/work/3564/")
    allURl.append("http://www.nippon-animation.co.jp/work/1928/")
    allURl.append("http://www.nippon-animation.co.jp/work/1920/")
    allURl.append("http://www.nippon-animation.co.jp/work/1916/")
    allURl.append("http://www.nippon-animation.co.jp/work/1912/")
    allURl.append("http://www.nippon-animation.co.jp/work/1906/")
    allURl.append("http://www.nippon-animation.co.jp/work/1871/")
    allURl.append("http://www.nippon-animation.co.jp/work/1855/")
    allURl.append("http://www.nippon-animation.co.jp/work/1847/")
    allURl.append("http://www.nippon-animation.co.jp/work/1839/")
    allURl.append("http://www.nippon-animation.co.jp/work/1811/")
    allURl.append("http://www.nippon-animation.co.jp/work/1777/")
    allURl.append("http://www.nippon-animation.co.jp/work/1722/")
    allURl.append("http://www.nippon-animation.co.jp/work/1709/")
    allURl.append("http://www.nippon-animation.co.jp/work/1700/")
    allURl.append("http://www.nippon-animation.co.jp/work/1696/")
    allURl.append("http://www.nippon-animation.co.jp/work/1688/")
    allURl.append("http://www.nippon-animation.co.jp/work/1674/")
    allURl.append("http://www.nippon-animation.co.jp/work/1670/")
    allURl.append("http://www.nippon-animation.co.jp/work/1654/")
    allURl.append("http://www.nippon-animation.co.jp/work/1644/")
    allURl.append("http://www.nippon-animation.co.jp/work/1640/")
    allURl.append("http://www.nippon-animation.co.jp/work/1636/")
    allURl.append("http://www.nippon-animation.co.jp/work/1597/")
    allURl.append("http://www.nippon-animation.co.jp/work/1578/")
    allURl.append("http://www.nippon-animation.co.jp/work/1569/")
    allURl.append("http://www.nippon-animation.co.jp/work/1554/")
    allURl.append("http://www.nippon-animation.co.jp/work/1550/")
    allURl.append("http://www.nippon-animation.co.jp/work/1546/")
    allURl.append("http://www.nippon-animation.co.jp/work/1542/")
    allURl.append("http://www.nippon-animation.co.jp/work/1528/")
    allURl.append("http://www.nippon-animation.co.jp/work/1524/")
    allURl.append("http://www.nippon-animation.co.jp/work/1520/")
    allURl.append("http://www.nippon-animation.co.jp/work/1507/")
    allURl.append("http://www.nippon-animation.co.jp/work/1503/")


    # kyoto animation
    allURl.append("http://www.kyotoanimation.co.jp/en/works/euphonium2/")
    allURl.append("http://www.kyotoanimation.co.jp/en/works/koeMovie/")
    allURl.append("http://www.kyotoanimation.co.jp/en/works/phantom/")
    allURl.append("http://www.kyotoanimation.co.jp/en/works/highspeed/")
    allURl.append("http://www.kyotoanimation.co.jp/en/works/kyokaiMovie/")
    allURl.append("http://www.kyotoanimation.co.jp/en/works/freeES/")
    allURl.append("http://www.kyotoanimation.co.jp/en/works/tamakoMovie/")
    allURl.append("http://www.kyotoanimation.co.jp/en/works/chuni02/")
    allURl.append("http://www.kyotoanimation.co.jp/en/works/kyokai/")
    allURl.append("http://www.kyotoanimation.co.jp/en/works/chuniMovie/")
    allURl.append("http://www.kyotoanimation.co.jp/en/works/free/")
    allURl.append("http://www.kyotoanimation.co.jp/en/works/tamako/")
    allURl.append("http://www.kyotoanimation.co.jp/en/works/chuni/")
    allURl.append("http://www.kyotoanimation.co.jp/en/works/hyouka/")
    allURl.append("http://www.kyotoanimation.co.jp/en/works/k-onMovie/")
    allURl.append("http://www.kyotoanimation.co.jp/en/works/nichijou/")
    allURl.append("http://www.kyotoanimation.co.jp/en/works/k-on02/")
    allURl.append("http://www.kyotoanimation.co.jp/en/works/haruhiDMovie/")
    allURl.append("http://www.kyotoanimation.co.jp/en/works/muntoMovie/")
    allURl.append("http://www.kyotoanimation.co.jp/en/works/k-on/")
    allURl.append("http://www.kyotoanimation.co.jp/en/works/muntoTV/")

    # A1-Picture
    allURl.append("http://a1p.jp/works/aobuta/")
    allURl.append("http://a1p.jp/works/saoa/")
    allURl.append("http://a1p.jp/works/fairytail2018/")
    allURl.append("http://a1p.jp/works/taizait/")
    allURl.append("http://a1p.jp/works/p5a/")
    allURl.append("http://a1p.jp/works/darlifra/")
    allURl.append("http://a1p.jp/works/taizaii/")
    allURl.append("http://a1p.jp/works/grancrest/")
    allURl.append("http://a1p.jp/works/blends/")
    allURl.append("http://a1p.jp/works/imass/")
    allURl.append("http://a1p.jp/works/fateapocrypha/")
    allURl.append("http://a1p.jp/works/fairytaildc/")
    allURl.append("http://a1p.jp/works/saenai2/")
    allURl.append("http://a1p.jp/works/eromanga/")
    allURl.append("http://a1p.jp/works/saom/")
    allURl.append("http://a1p.jp/works/raramagi/")
    allURl.append("http://a1p.jp/works/kuroshitsuji_m/")
    allURl.append("http://a1p.jp/works/aoexk/")
    allURl.append("http://a1p.jp/works/demi/")
    allURl.append("http://a1p.jp/works/occultic/")
    allURl.append("http://a1p.jp/works/utapurils/")
    allURl.append("http://a1p.jp/works/wworking/")
    allURl.append("http://a1p.jp/works/7taizais/")
    allURl.append("http://a1p.jp/works/qualidea/")
    allURl.append("http://a1p.jp/works/bpro/")
    allURl.append("http://a1p.jp/works/asterisk2/")
    allURl.append("http://a1p.jp/works/gyakusai/")
    allURl.append("http://a1p.jp/works/bhff15/")
    allURl.append("http://a1p.jp/works/doukyusei/")
    allURl.append("http://a1p.jp/works/p3m4/")
    allURl.append("http://a1p.jp/works/garakowa/")
    allURl.append("http://a1p.jp/works/grimgar/")
    allURl.append("http://a1p.jp/works/gate2/")
    allURl.append("http://a1p.jp/works/bokumachi/")
    allURl.append("http://a1p.jp/works/asterisk/")
    allURl.append("http://a1p.jp/works/kokosake/")
    allURl.append("http://a1p.jp/works/imasc2/")
    allURl.append("http://a1p.jp/works/gate/")
    allURl.append("http://a1p.jp/works/utapurir/")
    allURl.append("http://a1p.jp/works/guns/")
    allURl.append("http://a1p.jp/works/denpa/")
    allURl.append("http://a1p.jp/works/p3m3/")
    allURl.append("http://a1p.jp/works/nanohav/")
    allURl.append("http://a1p.jp/works/imasc/")
    allURl.append("http://a1p.jp/works/saenai/")
    allURl.append("http://a1p.jp/works/kuroshitsuji3_2/")
    allURl.append("http://a1p.jp/works/7taizai/")
    allURl.append("http://a1p.jp/works/kimiuso/")
    allURl.append("http://a1p.jp/works/magickaito/")
    allURl.append("http://a1p.jp/works/uchukyodaimovie/")
    allURl.append("http://a1p.jp/works/p4ga/")
    allURl.append("http://a1p.jp/works/aldnoahzero/")
    allURl.append("http://a1p.jp/works/sao2/")
    allURl.append("http://a1p.jp/works/nanana/")
    allURl.append("http://a1p.jp/works/fairytail2014/")
    allURl.append("http://a1p.jp/works/okii/")
    allURl.append("http://a1p.jp/works/idolmstermovie/")
    allURl.append("http://a1p.jp/works/zzz/")
    allURl.append("http://a1p.jp/works/magi2/")
    allURl.append("http://a1p.jp/works/anohana-movie/")
    allURl.append("http://a1p.jp/works/silverspoon/")
    allURl.append("http://a1p.jp/works/servantservice/")
    allURl.append("http://a1p.jp/works/saint023/")
    allURl.append("http://a1p.jp/works/oreimo-anime/")
    allURl.append("http://a1p.jp/works/utapri/")
    allURl.append("http://a1p.jp/works/vividred/")
    allURl.append("http://a1p.jp/works/oreshura/")
    allURl.append("http://a1p.jp/works/ao-ex-movie/")
    allURl.append("http://a1p.jp/works/magi/")
    allURl.append("http://a1p.jp/works/gyrozetter/")
    allURl.append("http://a1p.jp/works/shinsekaiyori/")
    allURl.append("http://a1p.jp/works/fairytail-movie/")
    allURl.append("http://a1p.jp/works/swordart-online/")
    allURl.append("http://a1p.jp/works/tsuritama/")
    allURl.append("http://a1p.jp/works/uchukyodai/")
    allURl.append("http://a1p.jp/works/idolmaster-anime/")
    allURl.append("http://a1p.jp/works/utapri1000/")
    allURl.append("http://a1p.jp/works/valkyria3-anime/")
    allURl.append("http://a1p.jp/works/ao-ex/")
    allURl.append("http://a1p.jp/works/anohana/")
    allURl.append("http://a1p.jp/works/fractale-anime/")
    allURl.append("http://a1p.jp/works/togainu/")
    allURl.append("http://a1p.jp/works/occult-gakuin/")
    allURl.append("http://a1p.jp/works/kuroshitsuji2/")
    allURl.append("http://a1p.jp/works/uchushow/")
    allURl.append("http://a1p.jp/works/1931tv/")
    allURl.append("http://a1p.jp/works/sorawoto/")
    allURl.append("http://a1p.jp/works/fairytail/")
    allURl.append("http://a1p.jp/works/valkyria-anime/")
    allURl.append("http://a1p.jp/works/birdy-tv2/")
    allURl.append("http://a1p.jp/works/nagisama-fc/")
    allURl.append("http://a1p.jp/works/kuroshitsuji/")
    allURl.append("http://a1p.jp/works/birdy-tv/")
    allURl.append("http://a1p.jp/works/persona-ts/")
    allURl.append("http://a1p.jp/works/namisuke/")
    allURl.append("http://a1p.jp/works/oofuri-1st/")
    allURl.append("http://a1p.jp/works/robikero/")
    allURl.append("http://a1p.jp/works/zenmaizamurai/")

    # randomly select one url
    myurl = random.choice(allURl)

    return myurl


"""
main() function only for test
"""
def main():
    myurl = selectURL()
    print(selectRegex(myurl))

if __name__ == "__main__":
    main()