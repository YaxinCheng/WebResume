import MongoKitten

struct MongoDB {
	private let mongoURI: String
	let cursor: Database?
	init() {
		mongoURI = "***REMOVED***"
		cursor = try? Database(mongoURL: mongoURI)
	}	
	
	func convertToDictionary(bson: Document) -> Dictionary<String, String> {
		var result = Dictionary<String, String>()
		for (key, value) in bson {
			result[key] = value is String ? value as! String : "\(value)"
		}
		return result
	}
}