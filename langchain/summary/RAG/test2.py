from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter


raw_doc = Document(
    page_content=(
        "无理由退货：普通数码配件支持签收后 7 天无理由退货，特殊商品除外。\n"
        "质量问题：如商品存在质量问题，需提交售后检测，检测通过后可维修、换货或退款。\n"
        "运费规则：非质量问题退货运费由用户承担，质量问题退货运费由商家承担。"
    ),
    metadata={
        "source": "after_sale_policy.md",
        "version": "2026-05",
        "category": "after_sale",
    },
)

splitter = RecursiveCharacterTextSplitter(
    chunk_size=60,
    chunk_overlap=10,
)

chunks = splitter.split_documents([raw_doc])

for index, chunk in enumerate(chunks):
    chunk.metadata["chunk_index"] = index
    print(chunk.page_content)
    print(chunk.metadata)