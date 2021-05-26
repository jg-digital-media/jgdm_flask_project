# Code Snippetss


## Filename tooltip

```css

& ~ .filename_tooltip {        
        
        background: black;
        display: none;
        color: white;
        padding: 5px;
        width: 200px;
        position: absolute;
        font-size: 10px;
        top: 20px;        

        &:hover {
            display: block;
            z-index: 1000
        }

    }
}

.image_container {
    position: relative;


    .filename_tooltip {
        background: black;
        display: none;
        color: white;
        padding: 5px;
        width: 200px;
        position: absolute;
        font-size: 10px;
        top: 20px;        

        &:hover {
            display: block;
            z-index: 1000
        }

        
    } 

```

## Tutorial Markup snippets

```html
<section class="container">    

    <h2> Photos Tutorial Page </h2>

     <!-- new tutorial container - double image -->   
    <article class="tutorial_container">

        <div class="image_container">
            
            <img src="../static/img/photos/IMG_4755.JPG" alt="" title="" class="photo" />
            
                                 
            <span class="filename_tooltip">Filename.JPG</span>                 

        </div>

        <div class="photo_details">

            <h3>Photos Content (1)</h3>

            <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Ex blanditiis, suscipit corrupti expedita sint impedit eligendi provident laborum officia similique. Sharpness - lots of sunlight. Slow moving flight</p>

            <p>Labore deserunt repellendus doloremque itaque tempora voluptas nihil hic repellat? </p>

        </div>  

        <div class="image_container">
            
            <img src="../static/img/photos/IMG_4755.JPG" alt="" title="" class="photo" />
            
                                 
            <span class="filename_tooltip">Filename.JPG</span>

        </div>

    </article>

    
            
    <div class="meta-data">
        <span><strong>Filename: </strong> name.JPG</span>
        <span><strong>ISO: </strong> 100 </span> 
        <span><strong>Shutter Speed: </strong> 1/500 </span>
        <span><strong>Aperture: </strong>f/8 </span>
        <span><strong>Focal Length: </strong> 300mm </span>

    </div>
    
    <div class="meta-data">
        <span><strong>Filename: </strong> name.JPG</span>
        <span><strong>ISO: </strong> 100 </span> 
        <span><strong>Shutter Speed: </strong> 1/500 </span>
        <span><strong>Aperture: </strong>f/8 </span>
        <span><strong>Focal Length: </strong> 300mm </span>

    </div>

    <hr />   

    <article class="tutorial_container">        

        <div class="image_container">
            
            <img src="../static/img/photos/IMG_4755.JPG" alt="" title="" class="photo" />
            
                                 
            <span class="filename_tooltip">Filename.JPG</span>     
                   

            <div class="photo_details">

                <h3>Photos Content (1)</h3>

                <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Ex blanditiis, suscipit corrupti expedita sint impedit eligendi provident laborum officia similique. Sharpness - lots of sunlight. Slow moving flight</p>

                <p>Labore deserunt repellendus doloremque itaque tempora voluptas nihil hic repellat? </p>

            </div>  
    
            <div class="meta-data">
                <span><strong>Filename: </strong> name.JPG</span>
                <span><strong>ISO: </strong> 100 </span> 
                <span><strong>Shutter Speed: </strong> 1/500 </span>
                <span><strong>Aperture: </strong>f/8 </span>
                <span><strong>Focal Length: </strong> 300mm </span>
        
            </div>        

        </div>


        <div class="image_container">
            
            <img src="../static/img/photos/IMG_4755.JPG" alt="" title="" class="photo" />
            
                                 
            <span class="filename_tooltip">Filename.JPG</span>

            <div class="photo_details">

                <h3>Photos Content (1)</h3>

                <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Ex blanditiis, suscipit corrupti expedita sint impedit eligendi provident laborum officia similique. Sharpness - lots of sunlight. Slow moving flight</p>

                <p>Labore deserunt repellendus doloremque itaque tempora voluptas nihil hic repellat? </p>

            </div>              
    
            <div class="meta-data">
                <span><strong>Filename: </strong> name.JPG</span>
                <span><strong>ISO: </strong> 100 </span> 
                <span><strong>Shutter Speed: </strong> 1/500 </span>
                <span><strong>Aperture: </strong>f/8 </span>
                <span><strong>Focal Length: </strong> 300mm </span>

            </div>

        </div>

    </article>

</section>
```