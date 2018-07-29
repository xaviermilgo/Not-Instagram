sleep=(ms)=>{
  return new Promise(resolve => setTimeout(resolve, ms));
};
async function nowsleep(x) {
  await sleep(x);
}}
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