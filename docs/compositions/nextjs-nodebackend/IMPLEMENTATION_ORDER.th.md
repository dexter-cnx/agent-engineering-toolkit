# ลำดับการลงมือทำ

## ลำดับที่แนะนำ
1. ตัดสินใจ scenario และขอบเขต
2. ใช้ `web-frontend-common` เพื่อกำหนด page state และพฤติกรรมฟอร์ม
3. ใช้ `web-frontend-nextjs` เพื่อวาง route และ boundary
4. ใช้ `backend-common` เพื่อกำหนด contract, validation, auth และ permissions
5. ใช้ `backend-node` เพื่อทำรายละเอียด runtime
6. เพิ่ม test และตรวจ flow ทั้งหมด

## ทำไมลำดับนี้ใช้ได้ผล
- ทำ contract ก่อน code
- ทำ boundary ให้ชัด
- frontend และ backend หลวมกันแต่ไม่หลุด
- review ง่ายขึ้นเพราะแต่ละชั้นมีหน้าที่เดียว

