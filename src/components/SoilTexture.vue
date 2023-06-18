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
                    <h3 class="title">Soil Texture</h3>
                    <button class="bg_btn mx-3" @click="toggleContent">{{ showContent ? 'Hide' : 'Show' }}</button>
                </div>
                <div v-show="showContent">
                    <p>
                        Soil texture is a fundamental aspect in the agronomic field, as it directly affects the soil's
                        fertility
                        and production capacity.<br>
                        This composition determines the physical and chemical characteristics of the soil that influence
                        plant
                        growth.<br> <br>
                        The first factor related to soil texture is pH: <br>
                        A soil with an alkaline pH between 8.2 and 8.8 is very often rich in limestone, generally soils of
                        this
                        type have a clayey texture, instead, a soil with an alkaline pH between 5 and 5.5, are generally
                        soils
                        with a sandy texture.
                        Soil pH is important because it affects the availability of <a
                            href="https://iastate.pressbooks.pub/introsoilscience/chapter/cec-aec/" target="_blank">nutrients</a> for
                        plants.
                        <br> <br>

                        Another important relationship is that between soil texture and electrical conductivity (Ec) and
                        sodium
                        absorption ratio (SAR), are indicators of soil
                        salinity and the presence of sodium, which can negatively affect plant growth if present in
                        excessive
                        amounts.
                        Too high values of these indicators are synonymous with soil
                        <a href="https://phycoterra.com/blog/soil-salinity-causes-affects-mitigation/">degradation</a> and
                        potential
                        <a href="https://www.unccd.int/land-and-life/desertification/overview">desertification.</a> <br>
                        <br>

                        Soil porosity represents the empty space between soil particles.
                        Porosity affects the soil's ability to hold water and air necessary for plant root growth. <br>
                        Sandy soils have a lower total porosity than clayey soils, but are usually well aerated because the
                        pores are large enough to allow water to drain. The greater aeration of sandy soils is therefore
                        associated with a lower water retention capacity. <br> <br>

                        The content of active calcium carbonate in soil is another texture-related factor that can influence
                        plant growth. <br>
                        Soils with a high content of active CaCO3 can bind nutrients, making them insoluble and
                        therefore unavailable to plants. This can limit crop growth and development. <br> <br>

                        The rate of degradation of the organic matter in the soil is also influenced by the texture, in
                        particular by the presence of clay and carbonates. <br>
                        Organic matter is essential for soil fertility, providing nutrients to plants and improving soil
                        structure. In clayey soils and with high carbonate contents, the organic matter can degrade more
                        slowly,
                        reducing the availability of nutrients for plants. <br> <br>
                        <span class="title">Understanding these relationships is essential for adopting sustainable soil
                            management
                            practices and responsible agricultural production.</span>
                    </p>

                    <div class="end_soiltext p-3">
                        <a href="#goup">^ Go Up ^</a>
                        <button class="bg_btn mx-3" @click="toggleContent">{{ showContent ? 'Hide' : ''}}</button>
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

