sleep=(ms)=>{
  return new Promise(resolve => setTimeout(resolve, ms));
};
async function nowsleep(x) {
  await sleep(x);
}