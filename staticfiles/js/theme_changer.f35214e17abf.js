var r = document.querySelector(':root');

$(document).ready(function(theme){
    change_theme("Pleasant");
});

function change_theme(theme){
    var rs = getComputedStyle(r);
    if (theme=='Pleasant'){
        r.style.setProperty('--currentTheme', "'Pleasant'");
        r.style.setProperty('--primaryColor', '#fff');  
        r.style.setProperty('--secondaryColor', '#fff');
        r.style.setProperty('--backgroundColor', '#F0E5D0');
        r.style.setProperty('--accentColor', '#DE3E33');
        r.style.setProperty('--primaryButtonColor', '#F0E5D0');  
        r.style.setProperty('--accentButtonColor', '#EC1C23');
        r.style.setProperty('--primaryTextColor', '#0d0d0d');
        r.style.setProperty('--secondaryTextColor', '#707070');
        r.style.setProperty('--primaryCardColor', '#2A333F');  
        r.style.setProperty('--footerBackgroundColor', '#2A333F');
        r.style.setProperty('--accentCardColor', '#BE3E35');
        r.style.setProperty('--footerCopyrightColor', '#222933');
        r.style.setProperty('--fadeColor', 'rgba(240, 229, 208, 0.5)');
        r.style.setProperty('--fadeHeader', 'rgba(0, 0, 0, 0.4)');
        r.style.setProperty('--cardBoxShadow', '0px 20px 99px rgb(190, 62, 53, 0.2)');
        r.style.setProperty('--companiesBoxShadow', '0px 5px 20px rgb(190, 62, 53, 0.1)');
        r.style.setProperty('--buttonBoxShadow', '0px 20px 99px rgb(190, 62, 53, 0.9)');
        
        document.getElementById('themeSwitcherIcon').src = "images/icons/smiling-face-outline.svg";
    
    }
    else if (theme=='Light') {
        r.style.setProperty('--currentTheme', "'Light'");
        r.style.setProperty('--primaryColor', '#0D0D0D');  
        r.style.setProperty('--secondaryColor', '#88898B');
        r.style.setProperty('--backgroundColor', '#FFFFFF');
        r.style.setProperty('--accentColor', '#DE3E33');
        r.style.setProperty('--primaryButtonColor', '#FFFFFF');  
        r.style.setProperty('--accentButtonColor', '#EC1C23');
        r.style.setProperty('--primaryTextColor', '#0d0d0d');
        r.style.setProperty('--secondaryTextColor', '#707070');
        r.style.setProperty('--primaryCardColor', '#FFFFFF');  
        r.style.setProperty('--footerBackgroundColor', '#2A333F');
        r.style.setProperty('--accentCardColor', 'none');
        r.style.setProperty('--footerCopyrightColor', '#222933');
        r.style.setProperty('--cardBoxShadow', '0px 20px 99px rgb(0, 0, 0, 0.1)');
        r.style.setProperty('--companiesBoxShadow', 'none');
        r.style.setProperty('--fadeColor', 'rgba(0, 0, 0, 0.2)');
        r.style.setProperty('--fadeHeader', 'rgba(0, 0, 0, 0.2)');
        r.style.setProperty('--buttonBoxShadow', '0px 20px 59px rgb(0, 0, 0, 0.14)');  
    
        document.getElementById('themeSwitcherIcon').src = "images/icons/sun-outline.svg";

    }
    else if (theme=='Dark') {
        r.style.setProperty('--currentTheme', "'Dark'");
        r.style.setProperty('--primaryColor', '#fff');  
        r.style.setProperty('--secondaryColor', '#bfbfbf');
        r.style.setProperty('--backgroundColor', '#1C2125');
        r.style.setProperty('--accentColor', '#DE3E33');
        r.style.setProperty('--primaryButtonColor', '#5C6165');  
        r.style.setProperty('--accentButtonColor', '#EC1C23');
        r.style.setProperty('--primaryTextColor', '#FFFFFF');
        r.style.setProperty('--secondaryTextColor', '#BFBFBF');
        r.style.setProperty('--primaryCardColor', '#33383C');  
        r.style.setProperty('--footerBackgroundColor', '#2A333F');
        r.style.setProperty('--accentCardColor', 'none');
        r.style.setProperty('--footerCopyrightColor', '#222933');
        r.style.setProperty('--cardBoxShadow', '0px 20px 99px rgb(0, 0, 0, 0.1)');
        r.style.setProperty('--companiesBoxShadow', 'none');
        r.style.setProperty('--fadeColor', 'rgba(27, 32, 36, 0.8)');
        r.style.setProperty('--fadeHeader', 'rgba(27, 32, 36, 0.8)');
        r.style.setProperty('--buttonBoxShadow', '0px 20px 59px rgb(0, 0, 0, 0.14)');  
    
        document.getElementById('themeSwitcherIcon').src = "images/icons/moon-outline.svg";

    }
}