pub struct Order {
    orderId: i32,
    total: f64,
    payment: Box<Payment>,
    product: Box<Product>,
}
