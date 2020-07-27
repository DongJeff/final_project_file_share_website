# final_project_file_share_website


## Backend
- Python3
- Django
- MongoDB

## Fronted
- Vue
- ElementUI
- Sass

## API
-  **All the success response code is 200**

### User
-  register
```shell script
POST http://127.0.0.1:8000/register/ {"username":'', "password":''}
```
![register](img/Snipaste_2020-07-28_01-13-27.png)

- login
```shell script
POST http://127.0.0.1:8000/login/ {"username":'', "password":''}
```
![login](img/Snipaste_2020-07-28_01-16-26.png)
**The token will be used every next request**

### Vip
- check the use is vip or not
```shell script
GET http://127.0.0.1:8000/vip/
headers:{'token':''}
```
![check vip](img/Snipaste_2020-07-28_01-20-26.png)

- top up to be a vip (just a simulate)
```shell script
POST http://127.0.0.1:8000/vip/  {"charge":10} 
headers:{'token':''}
```
![top up](img/Snipaste_2020-07-28_01-28-54.png)
**The charge mount must larger than 10$, or failed.**

If the user become a vip, than he/she can upload any size of file, or limited to 10MB. 

The file will be stored only 1 day if not vip , otherwise 30 days.

### File
- upload
```shell script
PUT http://127.0.0.1:8000/file/ {"file":fileobj}
headers:{'token':'','Content-Disposition':'attachment; filename="test1.mp4"'}
```
![upload header](img/Snipaste_2020-07-28_01-32-42.png)
![upload body](img/Snipaste_2020-07-28_01-32-50.png)
**The filename in the content-disposition will be used when download.**

- download
```shell script
GET http://127.0.0.1:8000/file/?share_code=
headers:{'token':''}
```
![download](img/Snipaste_2020-07-28_01-36-45.png)