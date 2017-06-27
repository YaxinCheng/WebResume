import MongoKitten

struct MongoDB {
	private let mongoURI: String
	let cursor: Database?
	init() {
		mongoURI = ""
		cursor = try? Database(mongoURL: mongoURI)
	}	
}
