-- lists all bands with Glam rock as their main style, ranked by their longevity

SELECT metal_bands.band_name, (COALESCE(split, CURDATE()) - formed) AS lifespan
FROM metal_bands WHERE style = 'Glam rock'
ORDER BY lifespan DESC
