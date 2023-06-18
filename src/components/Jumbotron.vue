<script>

export default {
    data() {
        return {

        };
    }
}

</script>



<template>
    <div id="goup" class="container my-5 txt_jumbo">
        <div class="row justify-content-center ">
            <div class="col-12 col-lg-8 col-md-8 bg_item rounded-4">
                <h1 class="title">Welcome</h1>
                <p>
                    In this project you will see using <span class="q_qgis">Q</span><span class="gis_qgis">GIS</span> and
                    the <span class="py_python">Py</span><span class="thon_python">thon</span> shell to come up with code
                    that will create a new
                    field in the layer's attribute table. This field will contain USDA texture grades, which will be based
                    on the composition of sand, silt, and clay in the soil.<br>
                    Once you have created the new field with USDA texture classes, you will see the mapping of texture
                    classes using Voronoi polygons. Voronoi polygons divide space based on proximity to data points.<br>
                    In this way it will be possible to visualize the various textural classes present in the area of
                    interest. <br>
                    The processing of the code to create the new field of texture classes will be done both using the QGIS
                    Python shell and the field calculator. <br>
                    You can find the Python code at my
                    <a style="color: #dd99fd; text-decoration: none;"
                        href="https://github.com/JungleKiosk/QGIS_SoilTexture/tree/main/py_code" target="_blank">GitHub</a>
                    page.
                    Enjoy!
                </p>
            </div>
        </div>

    </div>
</template>




<style>
.q_qgis {
    color: #ffab1a;
    font-weight: bold;
}

.gis_qgis {
    color: #bddf41;
    font-weight: bold;
}

.py_python {
    color: #fcd648;
    font-weight: bold;
}

.thon_python {
    color: #3da8ff;
    font-weight: bold;
}
</style>

