   async function getData() {
    try {
        const accessToken = sessionStorage.getItem('access_token');
        console.log(accessToken);

        // Make a GET request to the /admin endpoint with the access token in the headers
        const response = await fetch('http://127.0.0.1:5000/admin', {
            method: 'GET',
            headers: {
                'Authorization': `Bearer ${accessToken}`,
            },
        });

        console.log(response);

        if (response.ok) {
            let users = ''
            const data = await response.json();
            console.log('Data retrieved successfully!', data);
            for (var x in data.users) {
                   users = users + `<tr>
                        <td>${data.users[x]['username']}</td>
                        <td>${data.users[x]['email']}</td>
                        <td id="${data.users[x]['id']}"></td>
                    </tr>`;
}
         document.getElementById("users").innerHTML+=users
        } else if (response.status === 401) {

    
            console.error('Unauthorized access:', response.status);
            // Redirect to the login page or handle it in your way
            window.location.href = 'index.html';
        } else {
            window.location.href = 'index.html';
            console.error('Unexpected status code:', response.status);
        }
    } catch (error) {
        // Handle network errors or other issues
        console.error('Error:', error);
    }
}

async function getName(){
    try {
        const accessToken = sessionStorage.getItem('access_token');
        console.log(accessToken);

        // Make a GET request to the /admin endpoint with the access token in the headers
        const response = await fetch('http://127.0.0.1:5000/get_name', {
            method: 'GET',
            headers: {
                'Authorization': `Bearer ${accessToken}`,
            },
        });

        console.log(response);

        if (response.ok) {
            let users = ''
            const data = await response.json();
            console.log('Data retrieved successfully!', data);
            data.username
           
         document.getElementById("name").innerHTML+= data.username

        } else if (response.status === 401) {

    
            console.error('Unauthorized access:', response.status);
            // Redirect to the login page or handle it in your way
            window.location.href = 'index.html';
        } else {
            window.location.href = 'index.html';
            console.error('Unexpected status code:', response.status);
        }
    } catch (error) {
        // Handle network errors or other issues
        console.error('Error:', error);
    }
}

getData();
getName();
