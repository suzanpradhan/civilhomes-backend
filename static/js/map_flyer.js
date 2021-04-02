mapboxgl.accessToken =
  "pk.eyJ1Ijoic3V6YW5wcmFkaGFuIiwiYSI6ImNra3o1cHNoZDBhdGwycG1scTQ0ZWloaWYifQ.ALW63qccXjw6M07h3R0B5A";
var map = new mapboxgl.Map({
  container: "map",
  style: "mapbox://styles/mapbox/streets-v11",
  center: [85.31403, 27.6793064],
  zoom: 15.5,
  bearing: 27,
  pitch: 45,
});

var chapters = {
  "phaseI": {
    bearing: 27,
    center: [data.lat, 27.6793064],
    zoom: 15.5,
    pitch: 20,
    tabId: "phaseI_tab",
  },
  "phaseII": {
    duration: 6000,
    center: [85.3433958, 27.6846506],
    bearing: 150,
    zoom: 15,
    pitch: 0,
    tabId: "phaseII_tab",
  },
  "phaseIII": {
    bearing: 90,
    center: [85.32172421450346, 27.655816175472086],
    zoom: 13,
    speed: 0.6,
    pitch: 40,
    tabId: "phaseIII_tab",
  },
  "phaseIV": {
    bearing: 90,
    center: [85.3178252, 27.644261],
    zoom: 12.3,
    tabId: "phaseIV_tab",
  },
  "phaseV": {
    bearing: 27,
    center: [85.32733913170986, 27.668603037303523],
    zoom: 15.5,
    pitch: 20,
    tabId: "phaseV_tab",
  },
  "phaseVI": {
    duration: 6000,
    center: [85.32756441214282,27.672660306806865],
    bearing: 150,
    zoom: 15,
    pitch: 0,
    tabId: "phaseVI_tab",
  },
  "phaseVII": {
    bearing: 27,
    center: [85.34446238692404,27.676242369695238],
    zoom: 15.5,
    pitch: 20,
    tabId: "phaseVII_tab",
  },
  "phaseVIII": {
    bearing: 90,
    center: [85.34411904873664,27.66708268962151],
    zoom: 12.3,
    tabId: "phaseVIII_tab",
  },
  "phaseIX": {
    duration: 6000,
    center: [85.3385476568214, 27.659736765314086],
    bearing: 150,
    zoom: 15,
    pitch: 0,
    tabId: "phaseIX_tab",
  },
  "phaseX": {
    bearing: 90,
    center: [85.33310814726308,27.65623016778165],
    zoom: 12.3,
    tabId: "phaseX_tab",
  },
};

function scrollToElement(elementId) {
    // var positionX = 0;
    // var positionY = 0;

    while(elementId != null){
        positionY = positionY = document.getElementById('mapCards').offsetTop;
        // positionY = document.getElementById("mapCards").getBoundingClientRect().top;
        document.getElementById(elementId).scrollTo({top: positionY, behaviour: "smooth"});
    }
}

document.getElementById("mapCards").onscroll = function () {
  var chapterNames = Object.keys(chapters);
  for (var i = 0; i < chapterNames.length; i++) {
    var chapterName = chapterNames[i];
    if (isElementOnScreen(chapterName)) {
      setActiveChapter(chapterName);
      break;
    }
  }
};

var activeChapterName = "phaseI";
var activeTab = "phaseI_tab";
new mapboxgl.Marker({
    color: "#E61D1D",
  })
    .setLngLat(chapters[activeChapterName].center)
    .addTo(map);
function setActiveChapter(chapterName) {
  if (chapterName === activeChapterName) return;

  map.flyTo(chapters[chapterName]);

  document
    .getElementById(chapters[chapterName].tabId)
    .setAttribute("class", "active");
  document
    .getElementById(chapters[activeChapterName].tabId)
    .setAttribute("class", "");
  document.getElementById(chapterName).classList.add("active");
  document.getElementById(activeChapterName).classList.remove("active");

  new mapboxgl.Marker({
    color: "#E61D1D",
  })
    .setLngLat(chapters[chapterName].center)
    .addTo(map);

  activeChapterName = chapterName;
  activeTab = chapters[chapterName].tabId;
}

function isElementOnScreen(id) {
  var element = document.getElementById(id);
  var bounds = element.getBoundingClientRect();
  // console.log(document.getElementById("mapCards").getBoundingClientRect().top);
  // console.log(document.getElementById("mapCards").getBoundingClientRect().bottom);
  return (
    bounds.top < window.innerHeight &&
    bounds.bottom >
      document.getElementById("mapCards").getBoundingClientRect().top
  );
}
