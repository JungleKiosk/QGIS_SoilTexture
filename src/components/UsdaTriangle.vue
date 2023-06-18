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
    <div class="container my-5 txt_jumbo">
        <div class="row justify-content-center">
            <div class="col-12 col-lg-6 col-md-6 bg_item rounded-4">
                <div class="d-flex align-items-center p-3">
                    <h3 class="title">USDA Triangle</h3>
                    <button class="bg_btn mx-3" @click="toggleContent">{{ showContent ? 'Hide' : 'Show' }}</button>
                </div>
                <div v-show="showContent">
                    <p>
                        The <a
                            href="https://www.nrcs.usda.gov/resources/education-and-teaching-materials/soil-texture-calculator"
                            target="_blank">USDA
                            Texture Triangle</a> is a visual representation of the possible soil type combinations based on
                        soil particle size. Is used to classify soil texture in relative proportions of sand,
                        silt, and clay. <br>
                        The three legs represent the percentage of sand, silt, and clay in the
                        soil. La proporzione di ciascun componente viene rappresentata come una percentuale del totale.
                        For example, intersecting the following percentulai:
                    <ul>
                        <li>40% sand</li>
                        <li>40% silt</li>
                        <li>20% clay</li>
                    </ul>
                    you will score a point that falls in the area classified as Loam (Lo), which represents the
                    agronomically most suitable class.
                    </p>

                    <div class="row justify-content-center my-3">
                        <div class="col-12 col-lg-8 col-md-8 ">
                            <img class="rounded-5" src="./../assets/img/ex_use_usda.png" alt="">
                        </div>
                    </div>

                    <p>
                        Knowledge of soil texture via the USDA Texture Triangle enables farmers and soil experts to
                        implement specific management practices to improve soil fertility, irrigation, drainage, and crop
                        selection. It also helps assess soil erosion risk and plan soil conservation.
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
}
</style>

