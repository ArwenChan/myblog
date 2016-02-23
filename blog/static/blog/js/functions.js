var num=1;
var tag="";
var no_more=false;
var query="";
$("img").parents("p").css("text-align","center");// markdown can't do this

function fduoshuo() {
          var ds = document.createElement('script');
          ds.id = 'ds';
          ds.type = 'text/javascript';ds.async = true;
          ds.src = (document.location.protocol == 'https:' ? 'https:' : 'http:') + '//static.duoshuo.com/embed.js';
          ds.charset = 'UTF-8';
          (document.getElementsByTagName('head')[0] || document.getElementsByTagName('body')[0]).appendChild(ds);
}

function tagCheck (tagname) {
    var tags = document.getElementById("tag-area").getElementsByTagName("button");
    for(var i = 0, j = tags.length; i < j; i++)
    {
              tags[i].className = "btn btn-default btn-sm btn-round";
    }
    var thistag = document.getElementById(tagname);
    thistag.className = "btn btn-default btn-sm btn-round btn-round-chosen";
    
    query = "";
    $("#query_txt").val("");

    tag = tagname;
    num = 1;
    no_more = false;
    var blog_type = '';
    var href = window.location.href;
    var hrefs = href.split('/');
    if(hrefs.length==6){
        blog_type = hrefs[5];
    }
    $.get('/blog/tag-check',{'tag':tagname, 'blog_type':blog_type}, function(contentBlogs) {        
        $('#panel-body').html(contentBlogs);
    });
           
}



function moreBlog(){
    if(!no_more){
        var blog_type = '';
        var href = window.location.href;
        var hrefs = href.split('/');
        if(hrefs.length==6){
            blog_type = hrefs[5];
        }
        num = num + 1;
        $.get('/blog/more',{'blogs_number':num*10, 'query':query, 'tag':tag, 'blog_type':blog_type}, function(contentBlogs) {        
            $('#panel-body').html(contentBlogs);                            
        });
    }
    else{
        alert('没有更多咯！'); 
    }
}


$('#query_txt').bind('keypress', function(event) {
        if (event.keyCode == "13") {
            num = 1;
            no_more = false;
            tag = "";
            var tags = document.getElementById("tag-area").getElementsByTagName("button");
            for(var i = 0, j = tags.length; i < j; i++)
            {
                      tags[i].className = "btn btn-default btn-sm btn-round";
            }
            var querytxt = $("#query_txt").val();
            if(querytxt !== ''){
                query = querytxt;
                $.get('/blog/query',{'query':querytxt}, function(queryBlogs) { 
                        $('#panel-body').html(queryBlogs);});
            }
        }
});



function like(blog_id){
    $('#like').removeClass("icon-heart-empty");
    $('#like').addClass("icon-heart");
    $.get('/blog/addlike',{'blog_id':blog_id}, function(){});
}


/*function disreply(blog_id,father_id,num) {
    $('.reply').each(function(){
        if($(this).hasClass("hidden")){}
        else{$(this).addClass("hidden");}
    });
    var nameid = "replytxt" + num ;
    $('#'+nameid).removeClass("hidden");
    $('#'+nameid).val("");
    $('#'+nameid).keypress(function(event){
        if(event.keyCode == "13")    
            {
                freshCom(blog_id,father_id,nameid);                
            }
    });
} */ 
/*
function freshCom(blog_id, father_id, nameid){
    alert("稍后开放^_^");
    var com = '' ;
    if(father_id){
        com = $('#'+nameid).val();        
    }
    else{
        com = $('#comtxt').val();                
    }
    if(com !== ''){
        $.get('/blog/addcom',{'com':com, 'blog_id':blog_id, 'father_id':father_id}, function(listCom) {        
                    $('#comarea').html(listCom);});
    }   
    
}*/

