
//configures side bar button
document.querySelector('#sidebarCollapse').addEventListener('click',toggleSidebar);
var element = document.querySelector('#remove')

function toggleSidebar(){

    if (element.id == 'sidebar'){
        element.id = 'remove'
    }else { element.id = 'sidebar'}

}

//configures no bullshit button (this will remove any articles that reference donalnd trump)
document.body.querySelector('.bullshit').addEventListener('click', removeTrump);

function removeTrump(){

    // this will remove all signs of trump
    var all_articles = document.querySelectorAll('.article');
    all_articles.forEach(element =>{
        var text = element.innerText.toLowerCase()
        if (text.includes('trump')){
            element.remove()
        }
    })
}


var all_articles = document.querySelectorAll('.article')
var articles_array = Array.from(all_articles); //Converts nodelist to array
var article_container = document.querySelector('.article-row')

/**
 * Reorders the array - all headlines with no image
 * will get pushed to the end of the array
 */
articles_array.sort(function(a,b){
    const first = a.querySelector('img').getAttribute('src')
    const second = b.querySelector('img').getAttribute('src')

    if (first == second){
        return 0;
    }
    if(first == 'None'){
        return 1;
    }
    if (first != 'None'){
        return -1
    }
})

/**
 * For each element in the array
 * If there is no image, remove the broken url
 * and add each item of the previously ordered list
 * to it's parent element
 */
articles_array.forEach(element=>{
        var img_element = element.querySelector('img');
        if(img_element.getAttribute('src') == 'None'){
        img_element.remove();
    }
    article_container.append(element);
});
