select brand_name, lifespan from metal_bands where style='Glam rock' order by lifespan DESC;



SELECT band_name, isnull(split, 2022) - formed as lifespan FROM metal_bands
WHERE style LIKE '%Glam rock%' ORDER BY lifespan DESC;