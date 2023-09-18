const notificationsBtn = document.getElementById("notifications-btn");
const notificationsCount = document.getElementById("notifications-count");
const notificationsCont = document.getElementById("notifications-dropdown");

window.onload = () => {
  fetchNotifications();
  notificationsBtn.addEventListener("click", (e) => {
    markNotificationsAsRead();
  });

  setInterval(() => {
    fetchNotifications();
  }, 5000);
};


function fetchNotifications() {
  console.log("fetching")
  fetch("/alert-data/")
    .then((response) => response.json())
    .then((data) => renderNotifications(data))
    .catch((e) => console.log(e));
}

function renderNotifications(data) {
  notificationsCount.classList.toggle("hidden", true);
  let unReadCount = 0;
  let htmlData = "";
  if (data?.notifications) {
    data.notifications.forEach((notification) => {
      if (!notification?.read) {
        unReadCount++;
      }
      htmlData += getHtml(notification);
    });
    notificationsCont.innerHTML = htmlData;

    if (unReadCount > 0) {
      notificationsCount.classList.toggle("hidden", false);
      notificationsCount.innerText = unReadCount;
    }
  }
}

function getHtml(data) {
  const time = new Date(data?.created_at);
  return `
    <li>
      <a class="dropdown-item" href="#" style="${data?.read && 'background-color: #e9ecef;'}">
        <p class="text mb-0">${data?.message}</p>
        <p class="date text-muted mb-0"><small>${time.toLocaleString("en-us", {
          day: "2-digit",
          month: "long",
          year: "numeric",
        })} - ${time.toLocaleTimeString("en-us")}</small></p>
      </a>
    </li>
  `;
  // <small class="d-block">29 July 2020 - 02:26 PM</small>
}

function markNotificationsAsRead() {
  console.log("Mark Read");
  fetch("/mark-notifications-read/", { method: "POST" })
    .then((response) => response.json())
    .then((data) => fetchNotifications())
    .catch((e) => console.log(e));
}