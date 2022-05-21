


import qualified Data.ByteString as B
import qualified Data.Text as T
import Data.Text.Encoding (encodeUtf8, decodeUtf8)
import Data.Text

byteString :: String -> B.ByteString
byteString = encodeUtf8 . T.pack


textString :: B.ByteString -> Text
textString = decodeUtf8 


filename :: String
filename = "test2.hand"


main = do
    content <- readFile filename
    print $ "\128071"=="👇" 
    print $ "U+1F447" == "👇"
    print content
    -- print $ textString $ byteString content
    -- print $ byteString content

    return ()