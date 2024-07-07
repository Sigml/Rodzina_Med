let currentMonth = new Date().getMonth();
let currentYear = new Date().getFullYear();

function updateClock() {
    const now = new Date();
    const hours = now.getHours().toString().padStart(2, '0');
    const minutes = now.getMinutes().toString().padStart(2, '0');
    const seconds = now.getSeconds().toString().padStart(2, '0');
    document.getElementById('clock').innerText = `${hours}:${minutes}:${seconds}`;
}

function generateCalendar(month, year) {
    const months = ['Styczeń', 'Luty', 'Marzec', 'Kwiecień', 'Maj', 'Czerwiec', 'Lipiec', 'Sierpień', 'Wrzesień', 'Październik', 'Listopad', 'Grudzień'];
    const daysOfWeek = ['Pn', 'Wt', 'Śr', 'Cz', 'Pt', 'Sb', 'Nd'];
    const monthName = months[month];
    const daysInMonth = new Date(year, month + 1, 0).getDate();
    let calendarHtml = `<table><tr>`;

    for (const day of daysOfWeek) {
        calendarHtml += `<th>${day}</th>`;
    }
    calendarHtml += '</tr><tr>';

    const firstDayOfMonth = new Date(year, month, 1).getDay();
    const startDay = firstDayOfMonth === 0 ? 6 : firstDayOfMonth - 1; // Adjust for Monday start
    let day = 1;

    for (let i = 0; i < 42; i++) {
        if (i < startDay || day > daysInMonth) {
            calendarHtml += '<td></td>';
        } else {
            calendarHtml += `<td>${day}</td>`;
            day++;
        }
        if (i % 7 === 6) {
            calendarHtml += '</tr><tr>';
        }
    }
    calendarHtml += '</tr></table>';
    document.getElementById('calendar').innerHTML = calendarHtml;

    document.getElementById('current-month-year').innerText = `${monthName} ${year}`;
}

function prevMonth() {
    if (currentMonth === 0) {
        currentMonth = 11;
        currentYear--;
    } else {
        currentMonth--;
    }
    generateCalendar(currentMonth, currentYear);
}

function nextMonth() {
    if (currentMonth === 11) {
        currentMonth = 0;
        currentYear++;
    } else {
        currentMonth++;
    }
    generateCalendar(currentMonth, currentYear);
}

document.addEventListener('DOMContentLoaded', (event) => {
    updateClock();
    setInterval(updateClock, 1000);
    generateCalendar(currentMonth, currentYear);

    document.getElementById('prev-month').addEventListener('click', prevMonth);
    document.getElementById('next-month').addEventListener('click', nextMonth);
});
