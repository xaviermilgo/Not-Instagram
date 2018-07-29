sleep=(ms)=>{
  return new Promise(resolve => setTimeout(resolve, ms));
};
async function nowsleep(x) {
  await sleep(x);
}
document.onscroll = ()=>
    {
        if (document.body.scrollTop > 100 ) {
            $("#brand").removeClass("logo");
            $("#brand").addClass("mainicon");
        } else {
            $("#brand").removeClass("mainicon");
            $("#brand").addClass("logo");
        }
    };
choose= (id)=>{
  if ($("#likeicon"+id).hasClass("loved")){
      return unlike(id)
  }
  like(id)
};
like = (id)=>{
    $.get('/like/'+id,(newlikes)=>{
        anim=$("#likeheart"+id);
        anim.show(300);
        nowsleep(600).then(()=>{
                anim.hide(50);
                $("#likeicon"+id).addClass("loved")
                $("#likespan"+id).text(newlikes)
            }
        )
    });
};
unlike = (id)=>{
    $.get('/unlike/'+id,(newlikes)=>{
        nowsleep(600).then(()=>{
                $("#likeicon"+id).removeClass("loved");
                $("#likespan"+id).text(newlikes)
            }
        )
    });
};
togglefollow = (id)=>{
    $.get('/follow_or_not/'+id,(newfollows)=>{
        $("#following").text(newfollows[1]);
        $("#followers").text(newfollows[0]);
        let follow=$("#follow");
        let following=$("#follown");
        if (follow.hasClass("d-none")){
            follow.removeClass("d-none");
            following.addClass("d-none")
        }else{
            following.removeClass("d-none");
            follow.addClass("d-none")
        }
    });
};