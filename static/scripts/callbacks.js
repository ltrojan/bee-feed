function toggleEntry(emitter){
    console.log("Entry clicked!");
    console.log(emitter)
    txt = $(emitter).find(".entry-text")
    if (txt.hasClass('w3-hide')) {
	txt.removeClass('w3-hide')
    } else {
	txt.addClass('w3-hide')
    }
    
}
