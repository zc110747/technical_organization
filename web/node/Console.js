
function Console_process()
{
    //打印到stdout
    console.log('Console.js');
    console.log('%s.js', "Console");

    //打印到stderr
    //console.error(new Error('error'));
    
    const name = "Will";
    console.warn('Danger ${name}!Danger!');
}

Console_process();