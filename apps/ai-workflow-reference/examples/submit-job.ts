import { documentAnalysisJobPayloadSchema } from "@agent-toolkit/job-contracts";

const job = documentAnalysisJobPayloadSchema.parse({
  sourceUri: "https://example.com/invoice.pdf",
  documentType: "pdf",
  extractionTargets: ["invoiceNumber", "total", "dueDate"],
  instructions: "Extract invoice fields and keep the output JSON-safe.",
});

console.log(job);
