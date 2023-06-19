<script>
export default {
    data() {
        return {
            showContent: false, // Inizialmente nascondi il contenuto
        };
    },
    methods: {
        toggleContent() {
            this.showContent = !this.showContent; // Inverte lo stato di visualizzazione del contenuto
        },
    },
};
</script>


<template>
    <div class="container my-5 txt_jumbo ">
        <div class="row justify-content-center">
            <div class="col-12 col-lg-6 col-md-6 bg_item rounded-4">
                <div class="d-flex align-items-center justify-content-between p-3">
                    <h3 class="title">Voronoi: pros and cons</h3>
                    <button class="bg_btn mx-3" @click="toggleContent">{{ showContent ? 'Hide' : 'Show' }}</button>
                </div>
                <div v-show="showContent">
                    <p>
                        Using Voronoi polygons to map soil texture according to the USDA classification has both advantages
                        and disadvantages. <br>
                        Listed below are some pros and cons. <br> <br>

                        Pros: <br>
                        <hr>
                        1. Simplicity - The use of Voronoi polygons offers a simple method for mapping soil texture. The
                        creation of polygons can be automated and provides an immediate visual representation of the
                        distribution of textural classes. <br> <hr>
                        2. Spatial approximation - Voronoi polygons allow to obtain a good approximation of the presence of
                        USDA textural classes on the area of interest. Although texture is a continuous variable, polygons
                        can provide a rough representation of its distribution. <br> <hr>
                        3. Ease of interpretation - Voronoi polygons provide a clear graphical representation of the
                        different texture classes present in an area. This makes it easier to interpret and communicate soil
                        texture mapping results. <br> <hr> <br>

                        Cons: <br> <hr>
                        1. Simplification of spatial variability - Voronoi polygons simplify the spatial variability of soil
                        texture. Since texture is a continuous variable, the boundaries of polygons may not accurately
                        represent the transition between texture classes. This can lead to a loss of detail and information
                        on the actual distribution of textural classes. <br> <hr>
                        2. Dependence on the sampling point distribution - The accuracy of the Voronoi polygons depends on
                        the
                        sampling point distribution of the texture data. If the sampling points are not distributed
                        representatively or if they are concentrated in certain areas, this could affect the precision of
                        the polygons and the representation of textural classes. <br> <hr>
                        3. Limitations in representing complex areas: Voronoi polygons are suitable for representing regular
                        or relatively homogeneous areas. However, they may have difficulty representing areas with irregular
                        or complex boundaries. In such cases, the polygons may not fit perfectly with the real shape and
                        distribution of the textural classes. <br> <hr> <br>

                        In summary, using Voronoi polygons to map soil texture according to the USDA classification can
                        provide an approximate representation of the presence of texture classes on the parcel. However, it
                        is important to consider the limitations related to the simplification of the spatial variability
                        and the dependence on the distribution of the sampling points. If detailed representation of soil
                        texture is essential, it may be necessary to use more advanced approaches, such as interpolation or
                        the use of geostatistical models.
                    </p>



                    <div class="end_soiltext p-3">
                        <a href="#goup">^ Go Up ^</a>
                        <button class="bg_btn mx-3" @click="toggleContent">{{ showContent ? 'Hide' : '' }}</button>
                    </div>


                </div>
            </div>
        </div>
    </div>
</template>
  

<style>
.end_soiltext a {
    text-decoration: none;
    color: #aaaaaa;
}</style>

