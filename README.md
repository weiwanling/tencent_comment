# tencent_comment

## 腾讯视频评论爬虫实战(深度长评)
- 文件：xajh_cp.py
- 深度长评的URL地址格式为：https://video.coral.qq.com/filmreviewr/c/upcomment/[视频id]?&reqnum=3&commentid=[评论id]
- fildder
- requests-re
- 用户代理
-  [《新笑傲江湖》](https://v.qq.com/detail/4/4baf2nzoljqyobl.html)DVD版评论
-  抓包经过简化得到的url: https://video.coral.qq.com/filmreviewr/c/upcomment/4baf2nzoljqyobl?&reqnum=3&commentid=0

## 腾讯视频评论爬虫实战(短评)
- 文件：xajh_cp.py
- 全部短评评论的URL地址格式为：https://video.coral.qq.com/varticle/[视频编号]/comment/v2?&orinum=[返回评论个数]&cursor=[评论标号]"
- fildder
- requests-re
- 用户代理
-  [《新笑傲江湖》](https://v.qq.com/detail/4/4baf2nzoljqyobl.html)DVD版评论
-  抓包经过简化得到的url: https://video.coral.qq.com/varticle/1001103527/comment/v2?&orinum=12&cursor=0
