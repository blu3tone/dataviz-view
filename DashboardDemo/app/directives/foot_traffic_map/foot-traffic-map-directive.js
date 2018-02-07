'use strict';

angular.module('myApp.footTrafficMap', ['ngRoute'])
    .controller('FootTrafficMapController', ['$scope', '$timeout', '$filter', function($scope, $timeout, $filter) {
        $scope.i=0;
        $scope.minZoomLevel = 14;
        $scope.isPlay = false;
        $scope.delayTimeTmp = '1';
        $scope.delayTime = 1000;
        $scope.date = new Date("11/01/2017 00:00");
        $scope.defaultDate = angular.copy($scope.date);
        $scope.dateStr = $filter('date')($scope.date, "yyyy-MM-dd HH:mm");
        $scope.timeNode = 0;
        $scope.timeNodeMax = 720*2;
        $scope.timeNodeSliderOption = {
            value: 0,
            options: {
                floor: 0,
                ceil: 720
            }
        }
        $scope.delayTimeOptions = ['0.25', '0.5', '0.75', '1']
        $scope.timeNode = 0;
        $scope.updateTimeNode = function(){
            $scope.showMarker($scope.timeNode);
        }

        $scope.dateTimePickerConfig = {
            dropdownSelector: '#dropdown1',
            startView:'day',
            minView:'hour'
        }
        $scope.onTimeSet = function (newDate, oldDate) {
            $scope.matchDateToTimeNode();
        }
        var play = function(){
            $timeout(function(){
                $scope.timeNode++;
                $scope.matchTimeNodeToDate();
                if($scope.isPlay){
                    play();
                }
            }, $scope.delayTime)
        }
        $scope.start = function () {
            $scope.isPlay = !$scope.isPlay;
            if($scope.isPlay){
                play();
            }
        }

        $scope.setDelay = function () {
            $scope.delayTime = parseFloat($scope.delayTimeTmp) * 1000;
            $scope.isPlay = false;
        }
        $scope.matchTimeNodeToDate = function(){
            $scope.date.setTime($scope.defaultDate.getTime() + ($scope.timeNode *1000*60*60));
            $scope.dateStr = $filter('date')($scope.date, "yyyy-MM-dd HH:mm");
            $scope.drawFrame();
        }
        $scope.matchDateToTimeNode = function(){
            $scope.timeNode = ($scope.date.getTime() - $scope.defaultDate.getTime())/(1000*60*60);
            $scope.dateStr = $filter('date')($scope.date, "yyyy-MM-dd HH:mm");
            $scope.isPlay = false;
            $scope.drawFrame();
        }
        $timeout(function(){
            $scope.drawFrame();
        }, 1000)

    }]).directive('footTrafficMap', ['$timeout', function($timeout) {
    return {
        restrict: 'E',
        transclude: false,
        scope: {
        },
        templateUrl: "directives/foot_traffic_map/foot-traffic-map.html",
        controller: "FootTrafficMapController",
        link: function ($scope, element) {
            var map = new google.maps.Map(d3.select("#map").node(), {
                zoom: 14,
                center: new google.maps.LatLng(40.724768, -73.995173),
                mapTypeId: google.maps.MapTypeId.ROADMAP,
                disableDefaultUI: true,
                styles: [
                    {
                        "elementType": "geometry",
                        "stylers": [
                            {
                                "color": "#f5f5f5"
                            }
                        ]
                    },
                    {
                        "elementType": "labels.icon",
                        "stylers": [
                            {
                                "visibility": "off"
                            }
                        ]
                    },
                    {
                        "elementType": "labels.text.fill",
                        "stylers": [
                            {
                                "color": "#616161"
                            }
                        ]
                    },
                    {
                        "elementType": "labels.text.stroke",
                        "stylers": [
                            {
                                "color": "#f5f5f5"
                            }
                        ]
                    },
                    {
                        "featureType": "administrative.country",
                        "stylers": [
                            {
                                "visibility": "off"
                            }
                        ]
                    },
                    {
                        "featureType": "administrative.locality",
                        "stylers": [
                            {
                                "visibility": "off"
                            }
                        ]
                    },
                    {
                        "featureType": "administrative.neighborhood",
                        "stylers": [
                            {
                                "visibility": "simplified"
                            }
                        ]
                    },
                    {
                        "featureType": "administrative.province",
                        "stylers": [
                            {
                                "visibility": "off"
                            }
                        ]
                    },
                    {
                        "featureType": "landscape",
                        "stylers": [
                            {
                                "visibility": "simplified"
                            }
                        ]
                    },
                    {
                        "featureType": "poi",
                        "elementType": "geometry",
                        "stylers": [
                            {
                                "color": "#eeeeee"
                            }
                        ]
                    },
                    {
                        "featureType": "poi",
                        "elementType": "labels.text.fill",
                        "stylers": [
                            {
                                "color": "#757575"
                            }
                        ]
                    },
                    {
                        "featureType": "poi.attraction",
                        "stylers": [
                            {
                                "visibility": "simplified"
                            }
                        ]
                    },
                    {
                        "featureType": "poi.business",
                        "stylers": [
                            {
                                "visibility": "simplified"
                            }
                        ]
                    },
                    {
                        "featureType": "poi.government",
                        "stylers": [
                            {
                                "visibility": "simplified"
                            }
                        ]
                    },
                    {
                        "featureType": "poi.medical",
                        "stylers": [
                            {
                                "visibility": "simplified"
                            }
                        ]
                    },
                    {
                        "featureType": "poi.park",
                        "elementType": "geometry",
                        "stylers": [
                            {
                                "visibility": "simplified"
                            }
                        ]
                    },
                    {
                        "featureType": "poi.park",
                        "elementType": "labels.text.fill",
                        "stylers": [
                            {
                                "color": "#9e9e9e"
                            }
                        ]
                    },
                    {
                        "featureType": "poi.place_of_worship",
                        "stylers": [
                            {
                                "visibility": "simplified"
                            }
                        ]
                    },
                    {
                        "featureType": "poi.school",
                        "stylers": [
                            {
                                "visibility": "simplified"
                            }
                        ]
                    },
                    {
                        "featureType": "poi.sports_complex",
                        "stylers": [
                            {
                                "visibility": "simplified"
                            }
                        ]
                    },
                    {
                        "featureType": "road",
                        "elementType": "geometry",
                        "stylers": [
                            {
                                "color": "#ffffff"
                            }
                        ]
                    },
                    {
                        "featureType": "road.arterial",
                        "elementType": "labels.text.fill",
                        "stylers": [
                            {
                                "color": "#757575"
                            }
                        ]
                    },
                    {
                        "featureType": "road.highway",
                        "elementType": "geometry",
                        "stylers": [
                            {
                                "color": "#dadada"
                            }
                        ]
                    },
                    {
                        "featureType": "road.highway",
                        "elementType": "labels.text.fill",
                        "stylers": [
                            {
                                "color": "#616161"
                            }
                        ]
                    },
                    {
                        "featureType": "road.local",
                        "stylers": [
                            {
                                "visibility": "simplified"
                            }
                        ]
                    },
                    {
                        "featureType": "road.local",
                        "elementType": "labels.text.fill",
                        "stylers": [
                            {
                                "color": "#9e9e9e"
                            }
                        ]
                    },
                    {
                        "featureType": "transit.line",
                        "stylers": [
                            {
                                "visibility": "off"
                            }
                        ]
                    },
                    {
                        "featureType": "transit.station",
                        "elementType": "geometry",
                        "stylers": [
                            {
                                "color": "#eeeeee"
                            }
                        ]
                    },
                    {
                        "featureType": "water",
                        "elementType": "geometry",
                        "stylers": [
                            {
                                "color": "#c9c9c9"
                            }
                        ]
                    },
                    {
                        "featureType": "water",
                        "elementType": "labels.text.fill",
                        "stylers": [
                            {
                                "color": "#9e9e9e"
                            }
                        ]
                    }
                ]
            });

            var colorRange = ['#C3FF4D','#C9E74C','#D0D04B','#D7B94B','#DDA24A','#E48A4A','#EB7349','#F15C49','#F84548','#FF2E48'];
            // Read data
            var color = d3.scaleQuantile()
                .domain([0, 5000])
                .range(colorRange);

            $scope.data = [];

            var i = 0;

            while(i < 16){

                d3.json("data/foot-traffic-data-"+i+++".json", function (error, data) {

                    if (error) throw error;
                    $scope.data.push(data)

                });
            }



            //Create overlay
            var overlay = new google.maps.OverlayView();
            var heatmap = new HeatmapOverlay(map,
                {
                    // radius should be small ONLY if scaleRadius is true (or small radius is intended)
                    "radius": 0.001,
                    "maxOpacity": 0.5,
                    // scales the radius based on map zoom
                    "scaleRadius": true,
                    // if set to false the heatmap uses the global maximum for colorization
                    // if activated: uses the data maximum within the current map boundaries
                    //   (there will always be a red spot with useLocalExtremas true)
                    "useLocalExtrema": false,
                    // which field name in your data represents the latitude - default "lat"
                    latField: 'lat',
                    // which field name in your data represents the longitude - default "lng"
                    lngField: 'lon',
                    // which field name in your data represents the data value - default "value"
                    valueField: 'visitors'
                }
            );
            // Add the container when the overlay is added to the map.
            overlay.onAdd = function () {
                $scope.layer = d3.select(this.getPanes().overlayMouseTarget).append("div")
                    .attr("class", "stations");

                // Draw each marker as a separate SVG element.
                // We could use a single SVG, but what size would it have?
                overlay.draw = function () {
                    var projection = this.getProjection(),
                        padding = 10;

                    // var radialDefine = $scope.layer.enter().append("defs").append("radialGradient").attr("id", "grad");
                    // radialDefine.append("stop").attr("offset", "10%").attr("class", "center");
                    // radialDefine.append("stop").attr("offset", "80%").attr("class", "outer");
                    var marker = $scope.layer.selectAll("svg")
                        .data(d3.entries($scope.markerToDrawList))
                        .each(transform) // update existing markers
                        .enter().append("svg")
                        .each(transform)
                        .attr("class", "marker");
                    marker.append("circle")
                        .attr("r", 10)
                        .attr("cx", padding)
                        .attr("cy", padding)
                        .attr("fill", d => color(d.value['visitors']))
                        .on("click", togglePopup)
                        // .on("mouseover", expandNode)
                        // .on("mouseout", narrowNode);

                    function transform(d) {
                        d = new google.maps.LatLng(d.value['lat'], d.value['lon']);
                        d = projection.fromLatLngToDivPixel(d);
                        return d3.select(this)
                            .style("left", (d.x - padding) + "px")
                            .style("top", (d.y - padding) + "px");
                    }
                };
            };



            var contentString = '<div id="content">'+
                '<div id="siteNotice">'+
                '</div>'+
                '<h1 id="firstHeading" class="firstHeading">{0}</h1>'+
                '<div id="bodyContent">'+
                '<table>' +
                '<tr><td>Location: </td><td>{0}</td></tr>' +
                '<tr><td>Visitor: </td><td>{1}</td></tr>' +
                '<tr><td>Temperature: </td><td>{2}</td></tr>' +
                '<tr><td>WeatherSummary: </td><td>{3}</td></tr>' +
                '<tr><td>Events: </td><td>{4}</td></tr>' +
                '</table>'+
                '</div>'+
                '</div>';


            var infowindow = new google.maps.InfoWindow();


            function togglePopup(){
                var currentInfo = this.__data__.value;
                infowindow.setContent(contentString.format(currentInfo.location, currentInfo.visitors, currentInfo.temperature, currentInfo.weatherSummary, currentInfo.events));
                infowindow.setPosition({lat: currentInfo['lat'], lng: currentInfo['lon']});
                infowindow.open(map);
            }


            function expandNode() {
                d3.select(this).transition()
                    .duration(100)
                    .attr("r",15)
            };
            function narrowNode() {
                d3.select(this).transition()
                    .duration(100)
                    .attr("r",10)
            };

            // Bounds for Lower Manhattan
            var strictBounds = new google.maps.LatLngBounds(
                new google.maps.LatLng(40.699459910669994, -74.02263882031252),
                new google.maps.LatLng(40.74499453964404, -73.96942379345705));

            // Listen for the dragend event
            google.maps.event.addListener(map, 'dragend', function () {
                if (strictBounds.contains(map.getCenter())) return;

                // We're out of bounds - Move the map back within the bounds

                var c = map.getCenter(),
                    x = c.lng(),
                    y = c.lat(),
                    maxX = strictBounds.getNorthEast().lng(),
                    maxY = strictBounds.getNorthEast().lat(),
                    minX = strictBounds.getSouthWest().lng(),
                    minY = strictBounds.getSouthWest().lat();

                if (x < minX) x = minX;
                if (x > maxX) x = maxX;
                if (y < minY) y = minY;
                if (y > maxY) y = maxY;

                map.setCenter(new google.maps.LatLng(y, x));
            });
            // Limit the zoom level
            google.maps.event.addListener(map, 'zoom_changed', function () {
                if (map.getZoom() < $scope.minZoomLevel) map.setZoom($scope.minZoomLevel);
            });
            // Listen for the dragend event
            google.maps.event.addListener(map, 'dragend', function () {
                if (strictBounds.contains(map.getCenter())) return;

                // We're out of bounds - Move the map back within the bounds

                var c = map.getCenter(),
                    x = c.lng(),
                    y = c.lat(),
                    maxX = strictBounds.getNorthEast().lng(),
                    maxY = strictBounds.getNorthEast().lat(),
                    minX = strictBounds.getSouthWest().lng(),
                    minY = strictBounds.getSouthWest().lat();

                if (x < minX) x = minX;
                if (x > maxX) x = maxX;
                if (y < minY) y = minY;
                if (y > maxY) y = maxY;

                map.setCenter(new google.maps.LatLng(y, x));
            });
            overlay.onRemove = function(){
                $scope.layer.remove();
            }


            $scope.drawFrame = function () {
                $scope.markerToDrawList = [];
                var markerList = [];
                var timeToCompare = $scope.date.getTime();
                _.each($scope.data, function (dataList) {
                     var tmpList = _.filter(dataList, function (item) {
                        var tmpDate = new Date(item.beginningHour);
                        return tmpDate.getTime() == timeToCompare;
                    });
                    markerList.push(tmpList);
                });
                $scope.markerToDrawList = _.flatten(markerList, true);

                // Bind our overlay to the map…
                overlay.setMap(null);
                overlay.setMap(map);

                // Bind heat map
                heatmap.setData({max: 5000, data: $scope.markerToDrawList});
            }
            $scope.showMarker = function (index){
                var marker = $scope.layer.selectAll("svg");
                marker.attr("class", "marker hidden");
                marker[0][index].setAttribute("class", "marker");
            }
        }
    };
}]);

