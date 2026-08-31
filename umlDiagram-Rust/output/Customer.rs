pub struct Customer {
    username: String,
    email: String,
    address: String,
    phone: String,
    address: Box<Address>,
    order: Order,
}

impl User for Customer {
    // TODO: implement trait methods
}
