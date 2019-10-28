ymaps.ready(function () {
    var map = new ymaps.Map('map', {
        center: [59.939095, 30.315961],
        zoom: 10,
        controls: []
    });

	var myPlacemark1 = new ymaps.Placemark([59.951584, 30.328018], {
		iconContent: 'База "Рыбачок"'
	}, {
		preset: 'islands#darkOrangeStretchyIcon'
	});
	map.geoObjects.add(myPlacemark1);

	var myPlacemark2 = new ymaps.Placemark([59.862466, 30.131732], {
		iconContent: 'База "Русалочка"'
	}, {
		preset: 'islands#darkOrangeStretchyIcon'
	});
	map.geoObjects.add(myPlacemark2);

});