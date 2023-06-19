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
                    <h3 class="title">Processing Concept</h3>
                    <button class="bg_btn mx-3" @click="toggleContent">{{ showContent ? 'Hide' : 'Show' }}</button>
                </div>
                <div v-show="showContent">
                    <p>
                        For processing the code that maps texture classes to the USDA triangle, you can imagine the
                        percentages as map coordinates. <br>
                        With this approach you will then be able to identify points and create intervals to identify the
                        included area; i.e. the soil texture class. <br>
                        The image below shows the graphic identification one of the texture classes according to the
                        following logic:
                    </p>
                    <p class="text-center">
                        "Sand" &lt;= 65 AND "Sand" >= 45 AND  <br> "Clay" >= 35 AND "Clay" &lt;= 55 AND <br>
                        "Silt" >= 0 AND "Silt" &lt;= 20, 'SaCl',
                    </p>

                    <div class="row justify-content-center my-3">
                        <div class="col-12 col-lg-8 col-md-8 ">
                            <img class="rounded-5" src="./../assets/img/triangle_usda.png" alt="">
                        </div>
                    </div>

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
}
</style>

