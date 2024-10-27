async function fetchItems() {
    const url = "http://localhost:8000";

    try {
        const response = await fetch(url);
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data = await response.json();
        displayItems(data);
    } catch (error) {
        console.error("Error:", error);
    }
}

function displayItems(items) {
    const itemList = document.getElementById("membersList");

    itemList.innerHTML = "";

    items.forEach((item) => {
        const listItem = document.createElement("li");
        listItem.textContent = `${item.first_name} ${item.last_name} - ${item.role}`;

        const deleteButton = document.createElement("button");
        deleteButton.textContent = "Delete";
        deleteButton.onclick = function () {
            deleteItem(item.uuid); 
        };

        listItem.appendChild(deleteButton);
        itemList.appendChild(listItem);
    });
}

async function sendPostRequest() {
    const first_name = document.getElementById("fname").value;
    const last_name = document.getElementById("lname").value;
    const role = document.getElementById("role").value;

    if (!document.getElementById("privacyPolicy").checked) {
        alert("You must agree to the privacy policy before submitting.");
        return;
    }

    const data = {
        first_name: first_name,
        last_name: last_name,
        role: role
    };

    try {
        const response = await fetch("http://localhost:8000/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(data)
        });

        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }

        const responseData = await response.json();
        fetchItems();  
    } catch (error) {
        console.error('Error:', error);
    }
}

async function deleteItem(uuid) {
    const url = `http://localhost:8000/${uuid}`;

    try {
        const response = await fetch(url, {
            method: "DELETE",
        });

        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }

        const responseData = await response.json();
        fetchItems();  
    } catch (error) {
        console.error("Error:", error);
    }
}

window.addEventListener('load', function () {
    fetchItems();  
});
