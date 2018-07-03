import re
# html = """
#   <div class="movie-poster">
#         <img class="poster-default" src="//ms0.meituan.net/mywww/image/loading_2.e3d934bf.png">
#         <img src="http://p0.meituan.net/movie/f193e43ca706aa6bc6a26d6f53f0115a5315542.jpg@160w_220h_1e_1c">
#         <div class="movie-overlay movie-overlay-bg">
#           <div class="movie-info">
#             <div class="movie-score"><i class="integer">8.</i><i class="fraction">6</i></div>
#             <div class="movie-title movie-title-padding" title="超时空同居">超时空同居</div>
#           </div>
#         </div>
#       </div>
# """

# html = """
# <li class="pic-pack-out">
#             <a data-hrefexp="fr=wwwnews_index_newsarea_2_201410" href="http://www.1905.com/news/20180604/1285728.shtml?fr=wwwnews_index_newsarea_2_201410" target="_blank" class="pic-url">
#                 <img src="http://image11.m1905.com/uploadfile/2018/0604/thumb_1_150_100_20180604095110745921.jpg" title="《神奇马戏团》入围上影节 角逐金爵奖最佳动画片" alt="" height="100" width="150">
#                 <!--<i class="icon-corn">热</i>-->
#             </a>
#             <div class="pic-pack-inner">
#                 <h3><a data-hrefexp="fr=wwwnews_index_newsarea_2_201410" href="http://www.1905.com/news/20180604/1285728.shtml?fr=wwwnews_index_newsarea_2_201410" title="《神奇马戏团》入围上影节 角逐金爵奖最佳动画片" target="_blank" class="title ">《神奇马戏团》入围上影节 角逐金爵奖最佳动画片</a></h3>
#                 <p>6月3日，备受瞩目的第二十一届上海国际电影节组委会公布了本届金爵奖的入围名单。其中，动画电影《神奇马戏团》在一众优秀作品中脱颖而出、成...</p>
#                                 <div class="rel-other clear"><span class="timer fl">2018-06-04</span>
#                                         <a data-hrefexp="fr=wwwnews_index_newsarea_2_201410" class="type-url fl" target="_blank" href="http://www.1905.com/tag/tag-p-tagid-1287756.html?fr=wwwnews_index_newsarea_2_201410">神奇马戏团</a>
#                                                             <div class="share-btn fr icons" data-iframe="http://www.1905.com/api/share.php?id=1285728&amp;title=%E3%80%8A%E7%A5%9E%E5%A5%87%E9%A9%AC%E6%88%8F%E5%9B%A2%E3%80%8B%E5%85%A5%E5%9B%B4%E4%B8%8A%E5%BD%B1%E8%8A%82+%E8%A7%92%E9%80%90%E9%87%91%E7%88%B5%E5%A5%96%E6%9C%80%E4%BD%B3%E5%8A%A8%E7%94%BB%E7%89%87&amp;url=http%3A%2F%2Fwww.1905.com%2Fnews%2F20180604%2F1285728.shtml&amp;img=http%3A%2F%2Fimage11.m1905.cn%2Fuploadfile%2F2018%2F0604%2F20180604095110745921.jpg&amp;app_id=www&amp;sign=7e1a49e0f59e147128aa664d2294cac5">
#                         <div class="share-wrap"></div>
#                     </div>
#                 </div>
#                             </div>
#         </li>
# """

html = """
    <p class="abstract">
      文/麦大人 01 胡歌又刷屏了。 近日他上了《朗读者》，而这一期的主题是“生命”，他用磁性的嗓音，朗读了一段《哈姆雷特》中的经典独白，相当震撼：...
    </p>
"""

#a = re.compile('<div.*?movie-title.*?>(.*?)</div>',re.S)
#a = re.compile('<img\ssrc="(.*?)">',re.S)
#a = re.compile('<p>(.*?)</p>',re.S)
#a = re.compile('<h3><a.*?>(.*?)</a></h3>',re.S)
#a = re.compile('<img.?src="(.*?)">',re.S)

#a = re.compile('<li class=\"pic-pack-out\">(.*?)</li>',re.S).groups
#a = re.compile('<li.*?pic-pack-out">(.*?)</li>',re.S)
pattern = re.compile('<p.*?abstract.*?>(.*?)</p>',re.S)
b = re.findall(pattern,html)
print(b)