// Helper module to render same content accross multiple webpages, e.g. the header

const headerLinks = [
    {
        href: "/home",
        innerHTML: "Home"
    },
    {
        href: "/settings",
        innerHTML: "Settings"
    },
    {
        href: "/signout",
        innerHTML: "Sign Out"
    }
];

// Temporary, until back-end is integrated
const directChats = [
    {
        name: "Jonathan",
        img: "https://placeholder.co/40"
    },
    {
        name: "Lorem Ipsum",
        img: "https://placeholder.co/40"
    },
    {
        name: "Ratmir",
        img: "https://placehold.co/40"
    },
    {
        name: "Mom",
        img: "https://upload.wikimedia.org/wikipedia/commons/8/86/Woman_at_Lover%27s_Bridge_Tanjung_Sepat_%28cropped%29.jpg"
    }
]

// Temporary
const groups = [
    {
        name: "Year 4 Parents",
        img: "https://placeholder.co/50"
    },
    {
        name: "⭐Super Besties⭐",
        img: "https://placeholder.co/50"
    },
    {
        name: "Garage Sales LA",
        img: "https://placeholder.co/50"
    }
]

function renderHeader() {
    let header = document.createElement("header");
    let nav = document.createElement("nav");
    for (const a of headerLinks) {
        let link = document.createElement("a");
        [link.href, link.innerHTML] = [a.href, a.innerHTML];
        nav.appendChild(link);
    }
    header.appendChild(nav);
    document.body.prepend(header);
}

function renderDirectChats() {
    const chats = document.querySelector(".profile-preview-list");
    for (const chat of directChats) {
        let li = document.createElement("li");
        let span = document.createElement("span");
        span.className = "profile-preview-span";
        let img = document.createElement("img");
        img.src = chat.img;
        img.alt = "Placeholder image";
        img.width = "40";
        span.appendChild(img);
        let spanName = document.createElement("span");
        spanName.className = "profile-preview-name";
        spanName.textContent = chat.name;
        span.appendChild(spanName);
        li.appendChild(span);
        chats.appendChild(li);
    }
    if (directChats.length > 3) {
        let seeMore = document.createElement("li");
        seeMore.innerHTML = `<span class="profile-preview-span" id="profile-preview-list-see-more">See more...</span>`;
        chats.appendChild(seeMore);
    }
}

function renderGroups() {
    const groupsList = document.querySelector(".groups-preview-list");
    for (const group of groups) {
        let li = document.createElement("li");
        let span = document.createElement("span");
        span.className = "group-preview-span";
        let img = document.createElement("img");
        img.src = group.img;
        img.alt = "Placeholder image";
        img.width = "50";
        let spanName = document.createElement("span");
        spanName.className = "profile-preview-name";
        spanName.textContent = group.name;
        span.appendChild(spanName);
        span.appendChild(img);
        li.appendChild(span);
        groupsList.appendChild(li);
    }
}