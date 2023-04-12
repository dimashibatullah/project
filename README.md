
# Python Project Pacmann - Super Cashier

## A. Background Project
Semakin besar suatu perusahaan, maka dibutuhkan fasilitas yang lebih efektif dan efisien sehingga dapat menunjang kinerja dari perusahaan tersebut. Pada kasus ini, terdapat supermarket besar di salah satu kota di Indonesia yang memiliki suatu problem pada sistem pelayanannya. karena pada saat ini sistem pelayanan kasirnya dilakukan secara offline, sehingga jika di suatu hari terdapat banyak pembeli, maka  banyak custumer akan mengantri untuk melakukan pembayaran yang membuat sistem pelayanan kasirnya menjadi tidak efisien. oleh karena itu, pemilik dari perusahaan tersebut ingin melakukan improvement pada sistem pelayanan kasir sehingga customer yang tidak berada di kota supermarket tersebut tetap bisa membeli barang-barang disana. maka dari itu kami selaku programmer yang dipilih oleh pemilik supermarket tersebut untuk membuat program yang memudahkan custumer untuk melakukan pembelian.

## B. Requirements
* membuat fitur bagi customer untuk membuat id transaksi
* membuat fitur bagi customer untuk memasukan nama item, jumlah item dan harga per item pembelian
* membuat fitur bagi customer untuk update nama item jika terjadi kesalahan input nama item
* membuat fitur bagi customer untuk update jumlah item jika terjadi kesalahan input jumlah item
* membuat fitur bagi customer untuk update harga per item jika terjadi kesalahan input harga per item
* membuat fitur bagi customer untuk menghapus salah satu item
* membuat fitur bagi customer untuk menghapus seluruh item jika ingin melakukan pembatalan pembelian
* membuat fitur bagi customer untuk melihat seluruh pembelian
* membuat fitur bagi customer untuk menampilkan total harga pembelian setelah di potong jika mendapatkan diskon.Dengan ketentuan diskon sebagai berikut:
total belanja diatas Rp. 200000 ⇒ diskon 5%, total belanja diatas Rp. 300000 ⇒ diskon 8%, total belanja diatas Rp. 500000 ⇒ diskon 10%

## C. Flowchart
<img width="444" alt="flow chart" src="https://user-images.githubusercontent.com/128948493/230626067-b51dddc5-3905-4a82-91af-b452596aeeb2.png">

## D. Explanation Function
`add_item(nama item,  jumlah item, harga item)` = method yang digunakan untuk menambahkan item pembelian, kemudian itemnya di masukan ke sebuah list tabel

<img width="383" alt="def update item name" src="https://user-images.githubusercontent.com/128948493/230691154-325d4d34-a70c-457a-8b56-a65151999a66.png">


`update_item_name(nama item, update nama item)` = method yang digunakan untuk mengganti nama item yang ada di list pembelian

<img width="523" alt="def add item" src="https://user-images.githubusercontent.com/128948493/230690980-ca2b5f26-7336-4f29-b4cd-43b323981b88.png">





`update_item_qty(nama item, update jumlah item)` = method yang digunakan untuk mengganti jumlah item yang ada di list pembelian

<img width="402" alt="def update item qty" src="https://user-images.githubusercontent.com/128948493/230691272-058c06cc-3156-4401-a43c-b15f5c6eabc1.png">





`update_item_price(nama item, update harga item)` = method yang digunakan untuk mengganti harga item yang ada di list pembelian

<img width="430" alt="def update item price" src="https://user-images.githubusercontent.com/128948493/230691363-1b616a58-8efd-48e2-bb66-e619f4f1e850.png">





`delete_item(nama item)` = method yang digunakan untuk menghapus salah satu item beserta jumlah item dan harga per item nya

<img width="425" alt="def delete item" src="https://user-images.githubusercontent.com/128948493/230691395-8c48dafe-7c42-461f-ba42-00ef3f9167b9.png">





`reset_transaction()` = method yang digunakan untuk menghapus seluruh item pembelian

<img width="332" alt="def reser transaction" src="https://user-images.githubusercontent.com/128948493/230691426-bf34f0be-7a23-4060-9a92-8b85d3f6b9dc.png">





`check_order()` = method yang digunakan untuk menampilkan seluruh item pembelian

<img width="566" alt="def check order" src="https://user-images.githubusercontent.com/128948493/230691450-8e51bb90-ddd3-4484-91c2-7843d821e763.png">





`total_price()` = method yang digunakan untuk menghitung harga seluruh item pembelian serta dikurang dengan diskon jika total harga sesuai ketentuan

<img width="459" alt="def total_price1" src="https://user-images.githubusercontent.com/128948493/230691485-38290921-8453-4132-8936-4f9dcf0c8de2.png">

<img width="440" alt="def total_price2" src="https://user-images.githubusercontent.com/128948493/230691492-711d9444-7996-4a17-8e19-4109ce2becbf.png">


## E. Test Case Documentation

### Test 1
Customer ingin menambahkan dua item baru menggunakan method `add_item()`. Item yang ditambahkan adalah sebagai berikut:
* Nama item: Ayam Goreng, Qty: 2, Harga: 20000
* Nama item: Pasta Gigi, Qty: 3, Harga: 15000

Input:

<img width="264" alt="input test 1" src="https://user-images.githubusercontent.com/128948493/230749081-3013ed1f-d112-471b-8984-965138c58a62.png">


Output:

<img width="394" alt="output test 1" src="https://user-images.githubusercontent.com/128948493/230749088-d972e817-f4c8-4923-a3da-e73ee1d73a26.png">



### Test 2
Ternyata costumer salah membeli salah satu item dari belanjaan yang sudah ditambahkan, maka customer menggunakan method `delete_item` untuk menghapus item. Item yang ingin dihapus adalah Pasta Gigi.

Input:

<img width="260" alt="input test 2" src="https://user-images.githubusercontent.com/128948493/230749169-8f61ce16-5104-42ee-b51e-e7db01d597ee.png">


Output:

<img width="389" alt="output test 2" src="https://user-images.githubusercontent.com/128948493/230749175-c36f905d-36e6-4c49-9f9b-8c5f61ef725e.png">


### Test 3
Ternyata setelah dipikir-pikir customer salah memasukan item yang ingin dibelanjakan! Dari pada menghapusnya satu-satu, maka customer cukup menggunakan method `reset_transaction()` untuk menghapus semua item yang sudah ditambahkan.

Input:

<img width="258" alt="input test 3" src="https://user-images.githubusercontent.com/128948493/230749178-f66ce6bd-d997-462e-b411-3fce81061e30.png">


Output:

<img width="392" alt="output test 3" src="https://user-images.githubusercontent.com/128948493/230749181-9dfc985b-37dd-4ec7-a7d8-871488acf5e6.png">


### Test 4
Setelah customer selesai berbelanja, akan menghitung total belanja yang harus dibayarkan menggunakan method `total_price()`. Sebelum mengeluarkan output total belanja akan menampilkan item item yang dibeli

Input:

<img width="271" alt="input test 4" src="https://user-images.githubusercontent.com/128948493/230749184-58f087d7-3d38-449e-b5d8-ea24f05127af.png">


Output: 

<img width="641" alt="output test 4" src="https://user-images.githubusercontent.com/128948493/230749187-68648a84-ed6a-454b-a48b-15ddcbae1172.png">





