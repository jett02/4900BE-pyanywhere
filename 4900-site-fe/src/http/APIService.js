import axios from 'axios';
// Change the API_URL to the correct location of the backend API before deploying the app
const API_URL = 'http://127.0.0.1:8000/'; /* 'http://localhost:8000' http://127.0.0.1:8000/ or  'http://yourPythonAnywhereName.pythonanywhere.com/'*/

  export class APIService {
    constructor() {
      }
     getCustomer(param_pk) {
       const url = `${API_URL}/api/customers/${param_pk}`;
       let jwtToken = localStorage.getItem('access');
       const headers = {Authorization: `JWT ${jwtToken}`};
       return axios.get(url,  {headers: headers});
    }
  
     getCustomerList() {
      const url = `${API_URL}/api/customers/`;
      let jwtToken = localStorage.getItem('access');
      const headers = {Authorization: `JWT ${jwtToken}`};
      return axios.get(url,  {headers: headers});
    }
  
    addNewCustomer(customer){
     const url = `${API_URL}/api/customers/`;
     let jwtToken = localStorage.getItem('access');
     const headers = {Authorization: `JWT ${jwtToken}`};
     return axios.post(url, customer, {headers: headers});
    }
  
    updateCustomer(customer){
      const url = `${API_URL}/api/customers/${customer.pk}`;
      let jwtToken = localStorage.getItem('access');
      const headers = {Authorization: `JWT ${jwtToken}`};
       return axios.put(url, customer, {headers: headers});
    }
  
    deleteCustomer(customer_Pk){
       const url = `${API_URL}/api/customers/${customer_Pk}`;
       let jwtToken = localStorage.getItem('access');
       const headers = {Authorization: `JWT ${jwtToken}`};
       return axios.delete(url, {headers: headers});
    }
  
    authenticateLogin(credentials) {
      const url = `${API_URL}/api/`;
      return axios.post(url, credentials);
    }
  
   registerUser(credentials) {
      const url = `${API_URL}/register/`;
      credentials.customusername = credentials.username
      return axios.post(url, credentials);
    }
  
  }

