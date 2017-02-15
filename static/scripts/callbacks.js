function toggleEntry(txt){
    console.log("Entry clicked!");
    if (txt.hasClass('w3-hide')) {
	txt.removeClass('w3-hide')
    } else {
	txt.addClass('w3-hide')
    }
    
}
