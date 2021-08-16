mapboxgl.accessToken =
  "pk.eyJ1Ijoic3V6YW5wcmFkaGFuIiwiYSI6ImNra3o1cHNoZDBhdGwycG1scTQ0ZWloaWYifQ.ALW63qccXjw6M07h3R0B5A";
  
var map = new mapboxgl.Map({
  container: "map",
  style: "mapbox://styles/mapbox/streets-v11",
  center: [ongoingProjectsLocation[0].fields.longitude, ongoingProjectsLocation[0].fields.latitude],
  zoom: 15.5,
  bearing: 27,
  pitch: 45,
});
var chapters = {};

for (i = 0; i < ongoingProjectsJson.length; i++){
  chapters["phase" + ongoingProjectsJson[i].pk]=  {
    bearing: 27,
    center: [ongoingProjectsLocation[i].fields.longitude, ongoingProjectsLocation[i].fields.latitude],
    zoom: 15.5,
    pitch:20,
    tabId: "phase" + ongoingProjectsJson[i].pk + "_tab"
  };
}
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

var activeChapterName = "phase" + ongoingProjectsJson[0].pk;
var activeTab = "phase" + ongoingProjectsJson[0].pk + "_tab";
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
