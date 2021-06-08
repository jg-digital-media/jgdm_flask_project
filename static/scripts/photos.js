jQuery.getJSON('../static/data/data.json', function(photoData) { 

  
    let photo_list = photoData.photo_list.length;
    console.log(photoData.photo_list.length);

    for (let i=0; i < photo_list; i++) { 
        
        //successful delivery of class and image URL    - uses data-src and/or src attributes for image element        
        jQuery(`
        
            <li href="${photoData.photo_list[i].project_id} " target="blank"> 
            
            <strong>${photoData.photo_list[i].filename}</strong> - ${photoData.photo_list[i].description}

            </li>`

        ).appendTo('ul.list');     

   }

});