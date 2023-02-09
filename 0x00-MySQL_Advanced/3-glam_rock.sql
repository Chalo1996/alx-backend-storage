-- lists all bands with Glam rock as their main style, ranked by their longevity

SELECT metal_bands.band_name, ((split) - formed) AS lifespan
FROM metal_bands
WHERE style LIKE '%Glam rock%'
ORDER BY lifespan DESC
