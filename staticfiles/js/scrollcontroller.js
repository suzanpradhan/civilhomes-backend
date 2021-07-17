// function scrollToElement(elementId) {
//     // var positionX = 0;
//     // var positionY = 0;

//     while(elementId != null){
//         positionY = document.getElementById().offsetTop;
//         // positionY = document.getElementById("mapCards").getBoundingClientRect().top;
//         document.getElementById(elementId).scrollTo({top: positionY, behaviour: "smooth"});
//     }
// }

// function scrollController(elementId){
//     while(elementId != null){
//       console.log(elementId);
//      positionY = elementId.offsetTop;
//       document.getElementById('mapCards').scrollTo({top: positionY, behaviour: "smooth"});
//   }
// }

function scrollController(elementId){

    // Scrolls Card of Cards Section's scrollBar to the position of offestTopHeight of cards section.

    if(elementId != null){
      cardOffsetHeight = (elementId).offsetTop;
      cardsSectionOffsetHeight = document.getElementById("mapCards").offsetTop;
      console.log("cardOffsetHeight"+cardOffsetHeight);
      console.log("cardsSectionOffsetHeight"+cardsSectionOffsetHeight);
      console.log("total"+(cardOffsetHeight-cardsSectionOffsetHeight));
      document.getElementById('mapCards').scrollTo({top: (cardOffsetHeight - cardsSectionOffsetHeight), behaviour: "smooth"});
  }
}

function floorScrollController(elementId){

  // Scrolls Card of Cards Section's scrollBar to the position of offestTopHeight of cards section.

  if(elementId != null){
    floorOffsetLeft = (elementId).offsetLeft;
    floorSectionOffsetLeft = document.getElementById("siteViewPicture").offsetLeft;
    console.log("cardOffsetHeight"+floorOffsetLeft);
    console.log("cardsSectionOffsetHeight"+floorSectionOffsetLeft);
    console.log("total"+(floorOffsetLeft-floorSectionOffsetLeft));
    document.getElementById('siteViewPicture').scrollTo({left: (floorOffsetLeft - floorSectionOffsetLeft), behaviour: "smooth"});
}
}