import MongoKitten

struct MongoDB {
	private let mongoURI: String
	let cursor: Database?
	init() {
		mongoURI = "***REMOVED***"
		cursor = try? Database(mongoURL: mongoURI)
	}	
}